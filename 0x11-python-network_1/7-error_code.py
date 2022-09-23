#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
