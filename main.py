import urllib3
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('Stock_key')

def get_data():

    http = urllib3.PoolManager()
    url = f"https://cloud.iexapis.com/stable/stock/tsla/previous?token={API_KEY}"
    resp = http.request("GET", url)
    values = json.loads(resp.data)
    print(values)
    return values

get_data()