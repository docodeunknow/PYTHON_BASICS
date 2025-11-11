n = int(input("Enter the number :"))

for r in range(69, 64, -1):
    for s in range(69 - r):
        print(" ", end = "")
    for c in range(65, r + 1):
        print(chr(c), end = "")
    print()
