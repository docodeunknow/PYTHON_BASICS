# OPERATE OVERLOADING
try:
    class Number:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            # this runs when we use object1 + object2
            return Number(self.value + other.value)

    n1 = Number(10)
    n2 = Number(20)

except Exception as e:
    print(e)

else:
    result = n1 + n2 
    print(result.value)

finally:
    print("OPERATE OVERLOADING DONE !!") 