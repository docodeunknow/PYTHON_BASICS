i = 0 
x = 0
y = 1

n = int(input("Enter tha number for fibonacci series : "))

while i < n:
    z = x + y
    print(z)
    x=y
    y=z
    i += 1
