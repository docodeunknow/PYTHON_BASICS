n = int(input("Enter the number :"))

for r in range(69, 63, -1):
    for s in range(69 - r):
        print(" ", end = "")
    for c in range(63 - r, -1):
        print(chr(r), end = "")
    print()
    
