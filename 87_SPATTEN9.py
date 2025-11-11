n = int(input("enter the number :"))

for r in range(1, n+1, 1):
    for s in range(n - r):
        print(" ", end="")
    for c in range(r, 0, -1):
        print(c, end= "")
    print()
    
