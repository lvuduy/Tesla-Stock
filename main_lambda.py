import urllib3
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('Stock_key')

def get_data_lambda(event, context):
    http = urllib3.PoolManager()
    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={API_KEY}"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    return values