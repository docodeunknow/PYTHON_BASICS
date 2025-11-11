rev=0
num=int(input("Enter a Number for revers : "))

d=num%10
rev=(rev*10)+d
num = num//10

d=num%10
rev=(rev*10)+d
num = num//10

d=num%10
rev=(rev*10)+d
num = num//10

print(f"Your Revers number is :{rev}")