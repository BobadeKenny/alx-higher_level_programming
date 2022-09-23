#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys
if __name__ == "__main__":
    res = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(sys.argv[2], sys.argv[1]))
    res = res.json()
    try:
        for i in range(10):
            print("{}: {}"
                  .format(res[i]['sha'], res[i]['commit']['author']['name']))
    except IndexError:
        pass
