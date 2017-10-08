import xml.etree.ElementTree as ET
from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
url = input('Enter Location: ')
print('Retrieving',url)
data = urllib.request.urlopen(url).read()
data.decode()
tree = ET.fromstring(data)
print('Retrieved',len(data),'characters')
counts = tree.findall('.//count')
comm = tree.findall('comments/comment')
print('Count',len(counts))
s = 0
for count in comm:
    s = s + int(count.find('count').text)
print ('Sum',s)
