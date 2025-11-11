n = int(input("Enter the number : "))
temp = n 
rev = 0
for i in range(len(str(n))):
    d = n % 10
    rev = (rev *10 ) + d
    n //= 10

if temp == rev:
    print("your number is pelindrom ")
else:
    print("your number is not pelindrom ")