x=0
y=0
text = "X-DSPAM-Confidence:    0.8475";
x=text.find('0')
y=text.find('5')
v=text[x:y+1]
print(float(v))
