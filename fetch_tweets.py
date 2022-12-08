# Retrieve tweets
import requests
import json
import pandas as pd

import config

BEARER_TOKEN = config.BEARER_TOKEN

def get_tweets():
    url = "https://api.twitter.com/2/tweets?ids=1261326399320715264,1278347468690915330"

    headers = {}
    headers['Content-type'] = 'application/json'
    headers['User-Agent'] = 'language-meter'
    headers['Authorization'] = 'Bearer {}'.format(BEARER_TOKEN)

    resp = requests.get(url, headers=headers)
    json_data = json.loads(resp.text)

    with open('json/sample.json', 'w+') as out:
        json.dump(json_data, out)
        
if __name__ == "__main__":
    get_tweets()
