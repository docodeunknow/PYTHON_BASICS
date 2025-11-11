# LIST

# it's can tbe cangeed after create (mutable)
# duplicate value allow
# element are different datatype 

empty_list = []
int_list = [1,2,3,4,5]
str_list = ["apple", "banana", "charry"]
mix_list = [1,"hello", 3.14, True]
nested_list = [[1,2],[3,4],[5,6]]
float_list = [3.14, 3.21, 4.52]
complex_lsit = [1+3j,  1.+2j]

l1 = [1,2,3,4,5,6,7,8]
l2 = [9,0]

# operation

# 1 concation

print(l1+l2)

# 2 slicing

print(l1[1:4])
print(l1[:2])
print(l1[3:])
print(l1[-1])
print(l1[::-1])

# 3 true or False
#in and not in 

if 9 in l2:
    print("9 is present")

# method 

# lenth 

print(len(l1))

# max

print(max(l1))

# min

print(min(l2))

# sum 

print(sum(l1))

# count

print(l1.count(3))

# clear 

print(l2.clear())

# append 

print(l2.append(9))

#  insert 

# print(l2.insert(1,0))

# extraction 

# print(l1.extend(l2))

# remove
 
# print(l1.remove(8))

# index

print(l1.index(5))

# reverse

print(l1.reverse())

# copy 

# l3 = l1.copy()

# sort

print(l1.sort())
print(l1.sort(reverse=True))

print(type(l1))