class Student:
    def __init__(self,name,age,email,phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def display(self):
        print(f"name = {self.name}\nage = {self.age}\nemail ={self.email}\nphone number = {self.phone_number}")

class class_10(Student):
     def __init__(self,name,age,email,phone_number):
         super().__init__(name,age,email,phone_number)
     
     print("Admission Successful")


class class_12(Student):
    def __init__(self,name,age,email,phone_number):
        super().__init__(name,age,email,phone_number)

        if self.age >= 16:
            print("admission successful")
        else:
            print("admission failed")

print("press 1 for class 10th admission")
print("press 2 for class 12th admission")

choice = int(input("enter your choice"))

name = input("tell your name:-")
age = int(input("tell your age:-"))
email = input("tell your email:-")
phone = int(input("tell your number:-"))

if choice == 1:
    Student1 = class_10(name,age,email,phone)
    Student1.display()

if choice == 2:
    Student1 = class_12(name,age,email,phone)
    Student1.display()
 


# ak = Student("Deepak",21,"deepakkssm2020@gmail.com",8789165156)
# ak.display()
