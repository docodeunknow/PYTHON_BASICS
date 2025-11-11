n = int(input("Enter the number :"))

for r in range(70, 64, -1):
    for s in range(64 - r):
        print(" ", end = "")
    for c in range(69, r-1, -1):
        print(chr(r), end = "")
    print()
