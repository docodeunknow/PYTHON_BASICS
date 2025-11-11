n = int(input("Enter the number :"))

for r in range(65, 70, 1):
    for s in range(r - 65):
        print(" ", end = "")
    for c in range(70 - r):
        print(chr(r), end = "")
    print()
