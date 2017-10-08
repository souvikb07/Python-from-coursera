import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
# Retrieve all of the anchor tags
count = float(input('Enter count: '))
pos = float(input('Enter position: '))
def urlcall(c, p, link):
    if c < 0:
        return
    print('Retrieving:',link)
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href', None))

    c = c - 1
    urlcall(c, p, lst[int(p-1)])
urlcall(count, pos, url)
