# MULTILEVEL INHERINTANCE

try:
    # Grandparent class
    class Grandfather:
        def home(self):
            print("Grandfather has a small house.")

    # Parent class (inherits from Grandfather)
    class Father(Grandfather):
        def car(self):
            print("Father has a car.")

    # Child class (inherits from Father)
    class Son(Father):
        def bike(self):
            print("Son has a bike.")

except Exception as e:
    print(e)

else:
    s = Son()   

    s.home() 
    s.car()   
    s.bike()

finally:
    print("MULTILEVEL INHERINTANCE !!")