n = int(input("Enter the number :"))

for r in range(n, 0, -1):
    for s in range(n - r):
        print(" ", end = "")
    for c in range(r):
        print(r, end = "")
    print()
