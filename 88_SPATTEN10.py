n = int(input("enter the number :"))

for r in range(n, 0, -1):
    for s in range(r -1):
        print(" ", end="")
    for c in range(r, n +1, 1):
        print(c, end= "")
    print()
    
