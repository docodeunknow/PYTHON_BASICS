n = int(input("Enter the number :"))

for r in range(n, 0, -1):
    for s in range(r):
        print(" ", end = "")
    for c in range(n + 1, r , -1):
        print(r, end = "")
    print()
