#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])