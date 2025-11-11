# FILTER()

def fun(var):
    letter = ["a","b","c","d","e"]
    if var in letter:
        return True
    else :
        return False

seg = ["g","e","f","d","c"]

filtered = filter(fun, seg)

for s in filtered:
    print(s)