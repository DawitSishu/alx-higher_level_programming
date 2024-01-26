#!/usr/bin/python3
"""send a poost request and display the response"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    dta = parse.urlencode({"email": argv[2]}).encode('utf-8')
    with request.urlopen(argv[1], dta) as page:
        print(page.read().decode('utf-8'))
