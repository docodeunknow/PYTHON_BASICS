n = int(input("Enter the number :"))

for r in range(70, 64, -1):
    for s in range(r - 65):
        print(" ", end = "")
    for c in range(r, 70):
        print(chr(c), end = "")
    print()
