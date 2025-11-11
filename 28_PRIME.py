n = int(input("enter a number for check a prime number  : "))
c = 0
i = 1

while i <= n:
    if(n%i == 0):
        c += 1
    i += 1
if c > 2:
    print("your number is composition ")
else :
    print("your number is prime ")