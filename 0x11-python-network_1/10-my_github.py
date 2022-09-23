#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=basic)
    print(res.json().get("id"))
