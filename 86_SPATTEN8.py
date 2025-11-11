n = int(input("enter the number :"))

for r in range(n, 0, -1):
    for s in range(n - r):
        print(" ", end="")
    for c in range(1 , r + 1 ):
        print(c, end= "")
    print()
    
