from io import StringIO

import time
import json
import pandas as pd

def create_json_data(tweet_data):
    """
    Creates json data for loading into S3 Bucket
    """
    json_data = json.loads(tweet_data.content.decode(tweet_data.encoding))
    return json_data

def create_csv_data(tweet_data):
    """
    Creates csv data for loading into S3 bucket.
    """
    csv_data = pd.json_normalize(tweet_data, max_level=1) 
    csv_buffer = StringIO()
    csv_data.to_csv(csv_buffer, header=True, index=False)
    return csv_data

def create_json_path(language):
    """
    Specifies json path for S3 bucket
    """
    time_epoch = int(time.time())
    json_path = 'json/{}/{}'.format(language, time_epoch)
    return json_path

def create_csv_path(language):
    """
    Specifies csv path for S3 bucket
    """
    time_epoch = int(time.time())
    csv_path = 'csv/{}/{}'.format(language, time_epoch)
    return csv_path
