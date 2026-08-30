# harmless comment added during Revision B
# another harmless comment added during Revision B

import requests

def fetch_unsafe(url):
    return requests.get(url, verify=False)
