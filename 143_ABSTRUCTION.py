# ABSTRUCTION

from abc import ABC, abstractmethod

try:
    # Abstract class
    class Animal(ABC):

        @abstractmethod
        def sound(self):
            pass  # no details here → hidden

    # Child classes MUST define the sound
    class Dog(Animal):
        def sound(self):
            return "Bark"

    class Cat(Animal):
        def sound(self):
            return "Meow"

    d = Dog()
    c = Cat()

except Exception as e:
    print(e)

else:
    print(d.sound())   
    print(c.sound())

finally:
    print("ABSTRUCTION DONE !!")