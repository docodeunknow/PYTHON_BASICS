# Dictionary 

mydic = {
    "name" : "jay",
    "age" : 30,
    "height" : 5.7,
    "cooradinates" : (10, 20),
}

print(mydic.get("name"))

del mydic["age"]

key= mydic.keys()
values= mydic.values()
items= mydic.items()

print(key)
print(values)
print(items)

for k in mydic:
    print(k, mydic[k])