# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
values=0
s=0
count=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    values=tag.contents[0]
    #print('Contents:', values)
    s=s+int(values)
    count=count+1
print('sum', s)
print('count',count)

    #print('Attrs:', tag.attrs)
