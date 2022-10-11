largest = None
smallest = None
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try:
        num = int(number)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num
        
    if largest is None:
        largest = num
    elif largest < num:
        largest = num
           
print("Maximum is", largest)
print("Minimum is", smallest)   