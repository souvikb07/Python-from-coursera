
import urllib.request, urllib.parse, urllib.error
import json

url=input('Enter location:',)
print('Retrieving',url)
data = urllib.request.urlopen(url).read()
print('Retrieved',len(data),'characters')
s=0
info = json.loads(data)
for item in info['comments']:
    s=s+int(item['count'])
print('Count:', len(info['comments']))
print('Sum:',s)
