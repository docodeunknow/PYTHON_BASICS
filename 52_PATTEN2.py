##n = int(input("Enter the number: "))
##
##for i in range(5, 0, -1): 
##    for j in range(5 - i + 1): 
##        print(i, end="")  
##    print()  


n = int(input("Enter the number :"))

for i in range(n, 0, - 1):
    for j in range(0 ,n - i + 1):
        print(i, end="")
    print()
