# Retrieve tweets
import requests
import json

import config

class Results:
    """
    Class to handle pagination of results
    """
    
    def __init__(self, bearer_token, end_point=None, max_results=500) -> None:
        self.bearer_token = bearer_token
        self.max_results = max_results
        self.max_requests = 3
        self.total_results = 0
        self.n_requests = 0
        self.session = None
        self.next_token = None
        self.stream_started = False
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
        if self.session:
            self.session.close()
        
        self.session = requests.Session()
        headers = {
            'Content-type': 'application/json',
            'User-Agent': 'language-meter',
            'Authorization': 'Bearer {}'.format(self.bearer_token)}
        self.session.headers = headers
    
    def stream_results(self):
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
        self.current_tweets = None
        self.session.close()

    def make_request(self):
        resp = requests.get(url=self.endpoint, headers=self.headers)
        self.n_requests += 1
        resp = json.loads(resp.content.decode(resp.encoding))
        self.next_token = resp['meta']['next_token']
        self.current_tweets = resp['data']
    
    def write_json(self):
        with open('json/sample.json', 'w') as out:
            json.dump(self.current_tweets, out)

    def endpoint_builder(self):
        language = 'python'
        url = 'https://api.twitter.com/2/tweets/search/recent?query={}&max_results={}'.format(language, self.max_results)
        return url

if __name__ == "__main__":
    results = Results(bearer_token=config.BEARER_TOKEN, max_results=100)
    results.stream_results()