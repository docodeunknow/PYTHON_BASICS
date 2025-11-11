n = int(input("Enter the number : "))
x = 0
y = 1

for i in range(n):
    z = x + y
    print(z)
    x = y
    y = z
