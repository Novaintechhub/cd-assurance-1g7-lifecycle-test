import requests

def fetch_unsafe(url):
    return requests.get(url, verify=False)
