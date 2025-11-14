# CLASS & OBJECT

try:
    class student:
        def set_data(self, name, age):
            self.name = name
            self.age= age
    
        def show_data(self):
            print("name :", self.name)
            print("age :", self.age)

    s1 = student()
    s2 = student()

except Exception as e:
    print(e)

else:
    name =  input("Enter the  name :")
    age = int(input("Enter the age :"))
    s1.set_data(name, age)

    name =  input("Enter the  name :")
    age = int(input("Enter the age :"))
    s2.set_data(name, age)

    s1.show_data()
    s2.show_data()

finally:
    print("CLASS AND OBJECT DONE !!")