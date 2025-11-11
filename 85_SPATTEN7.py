n = int(input("enter the number :"))

for r in range(1, n + 1):
    for s in range(r):
        print(" ", end="")
    for c in range(n, r - 1, -1):
        print(c, end= "")
    print()
    
