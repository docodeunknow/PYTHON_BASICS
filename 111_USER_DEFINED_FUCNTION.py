# USER DEFINED FUNCTION

# 1. SIMPLE 

def sayhello():
    return "it's sayhello() function"
    
print(f"hello welacome to my simple function calling function {sayhello()}")

# 2. PARAMETER 

def result(n1, n2, n3):
    pares = (n1 + n2 + n3) / 3
    if  pares < 33:
        return "FAIL"
    else:
        return "PASS"

print(result(70,80,94))

# 3. PARAMETER WITH DEFFULT VALUES

def hello(name = "kill"):
    print(name)

hello()
hello("juli")
hello(name =  "leo")

# 3. INSIDE FUNCTION, NUMBER VARIABLE IS IMMUTABLE

def myfunc(x):
    print(f"value from recieved {x}")
    x = x + 1
    print(f"after agurment value of x is  : {x}")
    return

x  = 10 
print(f"value are x is pass is {x}")
myfunc(x)
print(f"after runing this function x value is {x}")

# 4. INSIDE FUNCTION LIST VARIAVBLE IS  MUTEBLE

def myf (ml):
    ml.append(40)
    print("inside of function is modified this list ")
    return

ml = [10, 20, 30]
print(f"befour this running function is list is {ml}")
myf(ml)
print(f"modifide list outside of a function is {ml}")