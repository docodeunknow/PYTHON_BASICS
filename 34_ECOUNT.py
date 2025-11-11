n = int(input("Enter a number :"))
ec = 0
esum = 0

while n >0:
    d = n % 10
    if n % 2 == 0:
        ec += 1
        esum += d
    n //= 10

print(f"YOur total number of digit is :{ec}")
print(f"sum of even digit in number :{esum}")