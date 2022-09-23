#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys
if __name__ == "__main__":
    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        r.raise_for_status()
        json = r.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
