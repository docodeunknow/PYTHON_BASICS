# NAMESCAPE 

def outter():
    a = 5 
    def inner():
        nonlocal a
        a = 10
    inner()
    print(a)
outter()

def out():
    a = 5 
    def inn():
        a =  10 
    inn()
    print(a)
out()