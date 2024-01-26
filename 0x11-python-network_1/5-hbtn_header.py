#!/usr/bin/python3
"""takes in a url and then sends a rewuest to it"""

import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
