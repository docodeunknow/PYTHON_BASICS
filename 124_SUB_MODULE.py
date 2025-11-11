import MAINMODULE 
import MAINMODULE as m
from MAINMODULE import mul # only mul function call 

n1 = int(input("enter the number 1 :"))
n2 = int(input("enter the number 2 :"))

print(f"your sum is : {MAINMODULE.sum(n1,n2)}")
print(f"your sub is : {m.sub(n1,n2)}")
print(f"your mul is : {MAINMODULE.mul(n1,n2)}")
print(f"your div is : {MAINMODULE.div(n1,n2)}")