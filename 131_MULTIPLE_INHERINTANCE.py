# MULTIPLE INHERINTANCE

try:
    # Parent class 1
    class Teacher:
        def teach(self):
            print("Teaching students")

    # Parent class 2
    class Writer:
        def write(self):
            print("Writing a book")

    # Child class inherits from both
    class Person(Teacher, Writer):
        pass 

except Exception as e:
    print(e)

else:
    p = Person()

    p.teach()
    p.write() 

finally:
    print("MULTIPLE INHERINTANCE!!")