# Retrieve tweets
import requests
from requests_oauthlib import OAuth1Session
from oauthlib.oauth2 import BackendApplicationClient
import json

import config

BEARER_TOKEN = config.BEARER_TOKEN

def get_tweets():
    url = "https://api.twitter.com/2/tweets?ids=1261326399320715264,1278347468690915330"

    headers = {}
    headers['Content-type'] = 'application/json'
    headers['User-Agent'] = 'language-meter'
    headers['Authorization'] = 'Bearer {}'.format(BEARER_TOKEN)

    resp = requests.get(url, headers=headers)
    print(resp.text)
    
if __name__ == "__main__":
    get_tweets()
