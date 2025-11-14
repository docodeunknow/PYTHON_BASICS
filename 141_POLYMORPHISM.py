# POLYMORPHISM

try:
    class Dog:
        def sound(self):
            return "Bark"

    class Cat:
        def sound(self):
            return "Meow"

    class Cow:
        def sound(self):
            return "Moo"


    # One function → many behaviors
    def animal_sound(animal):
        print(animal.sound())

    dog = Dog()
    cat = Cat()
    cow = Cow()

except Exception as e:
    print(e)

else:
    animal_sound(dog)   # Bark
    animal_sound(cat)   # Meow
    animal_sound(cow)   # Moo

finally:
    print("POLYMORPHISM DONE !!")