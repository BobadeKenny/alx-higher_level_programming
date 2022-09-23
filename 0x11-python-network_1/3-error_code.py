#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
