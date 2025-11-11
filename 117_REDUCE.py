# REDUCE

from functools import reduce

def mul(x,y):
    return x + y

num = [1,2,3,4,5]

pud = reduce(mul, num)

print(pud)