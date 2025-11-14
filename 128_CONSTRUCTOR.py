# CONSTRUCTOR


try:
    class student:
        def __init__(self,name,age, course):
            self.name = name
            self.age =  age
            self.course = course

        def show_info(self):
            print(f"Name is : {self.name}")
            print(f"age is : {self.age}")
            print(f"course is :{self.course}")
    
    name = input("enter the name : ")
    age = int(input("enter the  age :"))
    course = input("enter the course :")

    s1 = student(name, age, course)
    
except Exception as e:
    print(e)

else:
    s1.show_info()


finally:
    print("CONSTRUCTOR DONE !!")