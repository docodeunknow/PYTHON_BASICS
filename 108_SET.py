# SET

# mutable
# no index
# no suppet slicing

s1 = {"apple", "banana", "python", "java"}
s2 = {"data", "info"}
print(type(s1))

# Opareations

# 1 connection 

print(s1.union(s2))

# 2 intersection 

print(s1.intersection(s2))

# 3 difference 

print(s1.difference(s2))

# 4 summertric

print(s1.symmetric_difference(s2))

# method 

# add

print(s1.add("c++"))

# update

print(s1.update("c++", "c"))

# clear

# print(s2.clear())

# copy

s3 = s1.copy()

# discard

print(s3.discard("java"))

# remove

print(s3.remove("c"))

# pop (remove  by index)

p=s2.pop()
print(p)