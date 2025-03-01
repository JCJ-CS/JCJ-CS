largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    if largest is None:
        largest = num
    elif largest < num:
        largest = num

    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num

if largest is not None:
    print("Maximum is", largest)
if smallest is not None:
    print("Minimum is", smallest)