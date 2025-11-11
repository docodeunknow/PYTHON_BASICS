n = int(input("enter the number :"))

for r in range(1, n):
    for s in range(n - r):
        print(" ", end="")
    for c in range(2, r * 2 + 1, 2):
        print(c, end= "")
    print()
    
