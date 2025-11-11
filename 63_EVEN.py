n = int(input("Enter tha number :"))

for i in range(0, n + 1):
    for j in range(2, i * 2 + 1, 2):
        print(j, end="")
    print()