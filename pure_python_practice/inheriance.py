"""
class User:

    def login(self):
        print("Login")
    def register(self):
        print("Register")
class Student(User):
    def review(self):
        print("Review")
    def enroll(self):
        print("Enroll")

std1 = Student()
std1.login()
std1.register()
std1.enroll()
"""
"""
class Parent:
    def __init__(self, num):
        self.__num = num
    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,value,num):
        self.__val = value
    def get_val(self):
        return self.__val

son = Child(10,100)
print(son.get_val())
# print(son.get_num())-->create error because son constrctor is getting execute
"""

"""
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone's Constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy_phone(self):
        print("Buying a phone")
class Smartphone(Phone):

    def buy_phone(self):
        print("Buying a smart phone")
        super().buy_phone()
# by using super keyword we can get parent's constructor and methods
phone = Smartphone(20000,"apple",13)
phone.buy_phone()
"""
"""
class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone's Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
class Smartphone(Phone):
    def __init__(self,price,brand,camera,os,ram):
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside Smartphone's Constructor")
    def __str__(self):
        return (f"Brand: {self.brand}, Price: {self.price},Camera:{self.camera},OS:{self.os},RAM:{self.ram}")

phone = Smartphone(20000,"apple",13,"Mac",4)
print(phone)
"""
"""
class Parent:
    def __init__(self,num):
        self.__num= num
    def get_num(self):
        return self.__num
class Child(Parent):
    def __init__(self,num,val):
        super().__init__(num)
        self.__val = val
    def get_val(self):
        return self.__val
son = Child(200,300)
print(son.get_val())
print(son.get_num())

"""

class Parent:
    def __init__(self):
        self.num=100
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.val=200
    def show(self):
        print(self.val,self.num)
son = Child()
son.show()

# MRO--->Method resolution order...
#Polymorphisim-->
"""
1.Method overriding
2.Method overloading
3.Operator overloading
"""
"""

def area(radius):
    return 3.14*radius*radius
def area(length,breadth):
    return length*breadth
print(area(10))#Technically there is not method overlaoding in python
"""
class Geometry:

    def area(self,a,b=0):
        if b==0:
            print("Area of circle:",3.14*a*a)
        else:
            print("area of rectangle:",a*b)
obj = Geometry()
obj.area(10)
obj.area(10,20)
# by using default arguments we can do method overloading
