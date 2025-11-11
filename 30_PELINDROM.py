n = int(input("Enter a number for check Pelindrom : "))
r=0
t = n 

while n > 0:
    d = n % 10
    r = (r*10) + d
    n = n // 10

if r == t:
    print("Your number is pelindrom")
else:
    print("Your number is not pelindrom")