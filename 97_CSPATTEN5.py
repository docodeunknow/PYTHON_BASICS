n = int(input("Enter the number :"))

for r in range(65, 70):
    for s in range(70 - r):
        print(" ", end = "")
    for c in range(65, r + 1):
        print(chr(c), end = "")
    print()
