from io import StringIO

import json
import requests
import pandas as pd

import config

class Results:
    """
    Class to handle pagination of results
    """

    def __init__(
        self, bearer_token, end_point=None, max_query_results=100, max_results=500
        ) -> None:
        self.bearer_token = bearer_token
        self.session = None
        self.next_token = None
        self.stream_started = False
        self.max_results = max_results
        self.total_results = 0
        self.max_query_results = max_query_results
        self.max_requests = 3
        self.n_requests = 0
        self.current_tweets = None
  
        if end_point:
            self.endpoint = end_point
        else:
            self.endpoint = self.endpoint_builder()

        headers = {
            'Content-type': 'application/json',
            'User-Agent': 'language-meter',
            'Authorization': 'Bearer {}'.format(self.bearer_token)}
        self.headers = headers

    def init_session(self):
        """Initilizes requests session.

        Creates new requests session. Adds headers to the session.

        Args:
            self: Retrieving data from Results class

        Returns:
            None.
        """

        if self.session:
            self.session.close()

        self.session = requests.Session()
        headers = {
            'Content-type': 'applica:wtion/json',
            'User-Agent': 'language-meter',
            'Authorization': 'Bearer {}'.format(self.bearer_token)}
        self.session.headers = headers

    def stream_results(self):
        """Handles request results main logic loop.

        Makes Twitter API GET requests. Continues to make requests until
        the maximum number of requests or results is reached.
        """

        self.init_session()
        self.make_request()
        self.stream_started = True

        while True:
            for tweet in self.current_tweets:
                if self.total_results >= self.max_results:
                    break
                self.total_results += 1

            if self.next_token and self.total_results < self.max_results and self.n_requests < self.max_requests:
                self.make_request()
            else:
                break

        self.write_json()
        self.write_csv()
        self.current_tweets = None
        self.session.close()

    def make_request(self):
        """
        Makes Twitter API GET requests
        """

        resp = requests.get(url=self.endpoint, headers=self.headers)
        self.n_requests += 1
        resp = json.loads(resp.content.decode(resp.encoding))

        # Add error handling for KeyError 'meta'
        self.next_token = resp['meta']['next_token'] 

        self.current_tweets = resp['data']

    def write_json(self):
        """
        Writes request response to json.
        """

        with open('json/sample.json', 'w') as out:
            json.dump(self.current_tweets, out)
        # upload to S3 

    def write_csv(self):
        """
        Writes request response to csv file.
        """
        csv_data = pd.json_normalize(self.current_tweets, max_level=1) 
        csv_buffer = StringIO()
        csv_data.to_csv(csv_buffer, header=True, index=False)
        # upload to S3

    def endpoint_builder(self, id=None):
        """
        Creates target end point for API queries.
        """
        language = 'python'
        url = 'https://api.twitter.com/2/tweets/'
        if id:
            print('id is here')
        else:
            url = url + 'search/recent?query={}&max_results={}'.format(language, self.max_query_results)
        return url

if __name__ == "__main__":
    results = Results(bearer_token=config.BEARER_TOKEN)
    results.stream_results()
