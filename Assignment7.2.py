# Use the file name mbox-short.txt as the file name
count=0
num=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count=count+1
    s=line.find(' ')
    t=line[21:]
    t=float(t)
    num=num+t
    #print(t)
    #print(line)
print("Average spam confidence:",num/count)
