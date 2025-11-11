sum=0
num=int(input("Enter a 3 digit number : "))
d=num%10
sum=sum+d
num=num//10

d=num%10
sum=sum+d
num=num//10

d=num%10
sum=sum+d
num=num//10

print(f"Your 3 Digit addition is :{sum}")