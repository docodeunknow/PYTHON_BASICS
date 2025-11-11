n = int(input("enter the number :"))

for r in range(1, n +1, 1):
    for s in range(r - 1):
        print(" ", end="")
    for c in range(r, n +1):
        print(c, end= "")
    print()
    
