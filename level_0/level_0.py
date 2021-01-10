#!/usr/bin/python3
"""Method that votes 1024 times for an id on http site"""
import requests
""" Example of how to request HTTP to POST:

>>> payload = dict(key1='value1', key2='value2')
>>> r = requests.post("http://httpbin.org/post", data=payload)
>>> print(r.text)
{
  ...
  "form": {
    "key2": "value2",
    "key1": "value1"
  },
  ...
}
"""
url = 'http://158.69.76.135/level0.php'
voteBre = {'id': '2326', 'holdthedoor': 'Submit'}

for i in range(1024):
    r = requests.post(url, data=voteBre)

print(r.status_code, r.reason)