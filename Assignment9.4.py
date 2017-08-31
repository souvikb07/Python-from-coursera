name = input("Enter file:")
counts=dict()
words=list()
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
    line=line.rstrip()
    if not line.startswith('From '): continue
    wor=line.split()
    wor=wor[1]
    words.append(wor)
    #print(words)
for word in words:
        counts[word]=counts.get(word,0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)
