n = int(input("Enter the number :"))

for r in range(65, 70):
    for s in range(69 - r):
        print(" ", end = "")
    for c in range(r, 64, -1):
        print(chr(c), end = "")
    print()
