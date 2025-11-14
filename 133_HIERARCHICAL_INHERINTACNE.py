# HIERARCHICAL INHERITANCE

try:
    # Parent class
    class Animal:
        def sound(self):
            print("Animals make sounds.")

    # Child 1
    class Dog(Animal):
        def dog_sound(self):
            print("Dog barks.")

    # Child 2
    class Cat(Animal):
        def cat_sound(self):
            print("Cat meows.")

    # Child 3
    class Cow(Animal):
        def cow_sound(self):
            print("Cow moos.")

except Exception as e:
    print(e)

else:
    d = Dog()
    c = Cat()
    co = Cow()

    d.sound()       
    d.sound()       
    d.sound()       
    d.dog_sound()

    c.sound()       
    c.cat_sound()   

    co.sound()      
    d.sound()       
    co.cow_sound()

finally:
    print("HIERARCHICAL INHERITANCE DONE !!")