import re
sum=0
hand=open('regex_sum_20096.txt')
for line in hand:
    line=line.rstrip()
    stuff=re.findall( '[0-9]+',line)
    if not stuff: continue
    for number in stuff:
        sum =sum + float(number)
print(sum)
