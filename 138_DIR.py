# DIR()

try :
    class Student:
        def __init__(self):
            self.name = "Alice"
            self.age = 20

    s = Student()

except Exception as e:
    print(e)

else:
    print(dir(s))
 
finally:
    print("DIR() DONE !!!")

