#operation

str = "computer"
con = "sci"

# 1  joint

j = str + con
print(j)


# 2 repetition 

print(str * 3)


# 3 indexing

print(str[1])

# 4 slicing

print(str[1:4])
print(str[:2])
print(str[3:])
print(str[-1])
print(str[::-1]) #  useing reverse print




# methos

print("method")

# lenth

print(len(str))


# upercase

print(str.upper())
print(con.upper())

# lower case

print(str.lower())

# specified characters

s = "*python *"
print(s.strip("*"))

# specified delimite 

ss = "a s d f g h"
print(ss.split())

# capitalization 

print(str.capitalize())


# title

print(str.title())

# join

w = ["hello", "world"]
print(",".join(w))

# find

print(str.find("pu"))

# replace

r = "jinal"
print(r.replace("nal","gar"))

# count

c = "cououcnoucncounpooosdus"
print(c.count("o"))


# if you  check  your  condtion true or flase 

print(str.isupper())
print(str.islower())
print(str.isalpha())
print(str.isdigit())



