n = int(input("ENter the number : "))
c = 0

for i in range(n):
    if n % 2 == 0:
        c += 1

if c > 2:
    print(" number is composite ")
else:
    print("number is prime ")