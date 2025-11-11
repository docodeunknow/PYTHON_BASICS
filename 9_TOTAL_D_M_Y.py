d = int(input("Enter a number of day : "))

y = d // 365 
d = d % 365
m = d // 30
d = d % 30

print(f"Total number of the years is : {y}")
print(f"Total number of the months is : {m}")
print(f"Total number of the days is : {d}")