fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for i in words:
        if not i in lst:
            lst.append(i)
lst.sort()
print(lst)
