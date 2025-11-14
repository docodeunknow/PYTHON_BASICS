# SUPER()

try:
    class Parent:
        def show(self):
            print("Parent show() method")

    class Child(Parent):
        def show(self):
            super().show()   # call parent method
            print("Child show() method")

except Exception as e:
    print(e)

else:
    c = Child()
    c.show()

finally:
    print("SUPER() DONE!!")