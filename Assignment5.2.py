largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num=float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest=num
    elif smallest is None:
        smallest=num
    else:
        if num>largest:
             num=largest
        elif  num<smallest:
             num=smallest
    #print(num)
print("Maximum is", largest)
print("Minimum is", smallest)
