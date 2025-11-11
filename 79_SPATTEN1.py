n = int(input("Enter the number :"))

for r in range(1, n+1):
    for s in range(n - r):
        print(" ", end = "")
    for c in range(r):
        print(r, end = "")
    print()
