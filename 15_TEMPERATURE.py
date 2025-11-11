temp = int(input("Enter the hot temperature for check : "))

if temp>40:
    if temp>45:
        print("very hot")
    else:
        print("hot")
else:
    print("average")