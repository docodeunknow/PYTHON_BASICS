# MEGIC METHOD

try:
    class NumberBox:
        def __init__(self, value):
            # __init__ → runs when object is created
            self.value = value

        def __str__(self):
            # __str__ → controls what print() shows
            return f"NumberBox with value: {self.value}"

        def __len__(self):
            # __len__ → allows len(object)
            return len(str(self.value))   # length of digits (just an example)

        def __add__(self, other):
            # __add__ → allows object1 + object2
            return NumberBox(self.value + other.value)

        def __eq__(self, other):
        # __eq__ → allows object1 == object2
            return self.value == other.value


    a = NumberBox(50)
    b = NumberBox(70)

except Exception as e:
    print(e)

else:
    print(a)               # __str__
    print(b)               # __str__

    print(len(a))          # __len__
    print(len(b))          # __len__

    c = a + b              # __add__
    print(c)               # __str__

    print(a == b)          # __eq__
    print(a == NumberBox(50))   # __eq__

finally:
    print("MEGIC METHOD DONE!!!")