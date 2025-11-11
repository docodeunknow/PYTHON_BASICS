n =  int(input("Enter a number :"))
m = int(input("Enter a power"))
i = 1
p = 1
while i<=m:
    p *= n
    i +=1
    
print(f"your power : {p}")