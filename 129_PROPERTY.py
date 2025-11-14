# PROPERTY() METHODE

try: 
    class Student:

        def __init__(self, name):
            self._name = name   # _name means "private" by convention

        # getter method → to read the name
        def get_name(self):
            return self._name

        # setter method → to change the name
        def set_name(self, value):
            if len(value) < 3:
                print("Name is too short!")
            else:
                self._name = value

        # delete method → to delete the name
        def del_name(self):
            print("Deleting name...")
            del self._name

        # property() connects methods to an attribute name
        name = property(get_name, set_name, del_name)

except Exception as e:
    print(e)

else:
    s1 = Student("Alice")

    print(s1.name)   
    s1.name = "hir"  
    print(s1.name)

    s1.name = "Al"   
    del s1.name      

finally:
    print("PROPERTY DONE!!")
