n =  int(input("Enter a number :"))
m = int(input("Enter a power"))
i = 1
p = 1
for i  in range (m):
    p *= n
    i +=1
    
print(f"your power : {p}")