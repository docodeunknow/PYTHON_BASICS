# SINGLE_INHERINATANCE

try:
    # Parent class
    class Animal:   
        def eat(self):
            print("Animal can eat")

    # Child class (inherits from Animal)
    class Dog(Animal):
        def bark(self):
            print("Dog can bark")

except Exception as e:
    print(e)

else:
    d = Dog()
    d.eat()   
    d.bark() 

finally:
    print("SINGLE INHERINTANCE !!")