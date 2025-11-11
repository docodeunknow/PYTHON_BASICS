n = int(input("ENter a number for Armstrong : "))
s = 0
t = n

while n > 0:
    d = n % 10
    s = s + d * d * d
    n = n // 10 

if t == s:
    print("This number is Armstrong")
else:
    print("This number is not Armstrong")