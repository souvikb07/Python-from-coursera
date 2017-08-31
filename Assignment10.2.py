name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
counts=dict()
words=list()
handle = open(name)
for line in handle:
    if not line.startswith('From '): continue
    wor=line.split()
    wor=wor[5]
    wor=float(wor[0:2])
    words.append(wor)
    #print(words)
for word in words:
    counts[word]=counts.get(word,0)+1
#print(sorted([(k,v) for k,v in counts.items()])) This will print as a Tuple
lst=list()
for k,v in counts.items():
    tup=(k,v)
    lst.append(tup)
lst.sort()
for k,v in lst:
    print(k,v)
