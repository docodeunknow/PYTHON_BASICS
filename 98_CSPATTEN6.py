n = int(input("Enter the number :"))

for r in range(69, 64, -1):
    for s in range(r - 64):
        print(" ", end = "")
    for c in range(69, r - 1, -1):
        print(chr(c), end = "")
    print()
