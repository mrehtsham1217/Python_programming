class Atm:
    __Counter = 1
    #object._Classname__variable_name.--->can access private varibale
    #instance varibale -->value is different for every object
    def __init__(self):
        #what is self--->cureent working object is called self
        #declare private variable by using __
        self.__pin = ""
        self.__balance = 0
        self.serial_no = Atm.__Counter
        Atm.__Counter = Atm.__Counter+1
        #self.menu()
        # print(id(self))
        #we use to write the code in constructor that we want to see when app
        #opens--->atm has by default cash withdrawl option,transer and etc
        # that executes automatically--->no user control
    @staticmethod
    def get_counter():
        return Atm.__Counter
    @staticmethod
    def set_counter(new):
        if type(new)==int:
            Atm.__Counter = new
        else:
            print("Not allowed")

    def menu(self):
        user_input = input("""
        Hello how you want to procoeed
        1.Enter 1 to create Pin
        2.Enter 2 to deposit cash
        3.Enter 3 to withdraw cash
        4.Enter 4 to check balance
        5.Enter 5 to exit
        """)
        if user_input =='1':
            self.create_pin()
        elif user_input=='2':
            self.dospit_cash()
        elif user_input=='3':
            self.withdrawl_cash()
        elif user_input=='4':
            self.check_balance()
        elif user_input=='5':
            self.exit_func()
        else:
            print("Incorrect input")
    def create_pin(self):
        self.__pin = input('Enter your pin')
        print("Pin set successfully--!")
    def dospit_cash(self):
        temp = input("Enter your pin--!")
        if temp==self.__pin:
            amount = int(input("Enter your amount"))
            self.__balance = self.__balance + amount
            print("Balance dospited succesfully--!")
        else:
            print("invalid pin")
    def withdrawl_cash(self):
        temp = input("Enter your pin--!")
        if temp == self.__pin:
            amount = int(input("Enter your amount"))
            if amount <= self.__balance:
                self.__balance = self.__balance-amount
                print("Cash withdrawl successfully---!")
            else:
                print("Insufficinet balance")
        else:
            print("Invalid pin")
    def check_balance(self):
        temp = input("Enter your pin--!")
        if temp == self.__pin:
            print("Total balance is:  " ,self.__balance)
        else:
            print("Invalid pin--!")
    def exit_func(self):
        print("Thanku for using Allied Services:")
        exit()
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        if type(new_pin)==str:
            self.__pin = new_pin
            print("Pin changed:")
        else:
            print("Not allowed--!Enter a string")

class Fraction:
    def __init__(self,n,d):
        self.nom = n
        self.denom = d

    def __str__(self):
        return "{}/{}".format(self.nom,self.denom)

    def __add__(self, other):
        temp_nom = self.nom*other.denom+self.denom*other.nom
        temp_denom = self.denom*other.denom
        return "{}/{}".format(temp_nom,temp_denom)

    def __sub__(self, other):
        temp_nom = self.nom*other.denom-self.denom*other.nom
        temp_denom = self.denom*other.denom
        return "{}/{}".format(temp_nom,temp_denom)

    def __mul__(self, other):
        temp_nom = self.nom*other.nom
        temp_denom = self.denom*other.denom
        return "{}/{}".format(temp_nom,temp_denom)


    def __truediv__(self, other):
        temp_nom = self.nom * other.denom
        temp_denom = self.denom * other.nom
        return "{}/{}".format(temp_nom, temp_denom)

class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
def greet(customer):
    if customer.gender == 'male':
        print("hello",customer.name,"Sir")
    else:
        print("Hello",customer.name," Maa'm")

    cust3 = Customer("Mumza","male")
    return cust3
# call by referencing
class Student:
    def __init__(self,name):
        self.name = name
def greet(customer):
    customer.name = "Ehtsham"
    print(customer.name)

if __name__=="__main__":
    Atm.get_counter()
    Atm.set_counter("wwww")
    obj1 = Atm()
    print(obj1.serial_no)
    obj2 = Atm()
    print(obj2.serial_no)
    obj3 = Atm()
    print(obj3.serial_no)
    obj4 = Atm()
    print(obj4.serial_no)
    obj5 = Atm()
    print(obj5.serial_no)


    # std = Student("Fatima")
    # greet(std)
    #print(std.name)
    """
    cust = Customer("Ehtsham",'male')
    cust2 = Customer("Fatima",'female')
    new_cust3 = greet(cust2)
    print(new_cust3.name,new_cust3.gender)
    greet(cust2)
    greet(cust)
"""

"""
    obj = Atm()
    print(id(obj))
    obj.dospit_cash()
    obj.withdrawl_cash()
    obj.check_balance()
    obj1 = Fraction(5,6)
    # print(obj1)

    # obj2 = Fraction(7, 8)
    #print(obj2)

    # print("Addition: ",obj1+obj2)
    # print("Subtraction",obj1-obj2)
    # print("Multiplication:",obj1*obj2)
    # print("Division: ",obj1/obj2)
"""
