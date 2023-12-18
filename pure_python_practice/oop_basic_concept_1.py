class Atm:
    def __init__(self):
        #what is self--->cureent working object is called self
        self.pin = ""
        self.balance = 0
        self.menu()
        print(id(self))
        #we use to write the code in constructor that we want to see when app
        #opens--->atm has by default cash withdrawl option,transer and etc
        # that executes automatically--->no user control
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
        self.pin = input('Enter your pin')
        print("Pin set successfully--!")
    def dospit_cash(self):
        temp = input("Enter your pin--!")
        if temp==self.pin:
            amount = int(input("Enter your amount"))
            self.balance = self.balance + amount
            print("Balance dospited succesfully--!")
        else:
            print("invalid pin")
    def withdrawl_cash(self):
        temp = input("Enter your pin--!")
        if temp == self.pin:
            amount = int(input("Enter your amount"))
            if amount <= self.balance:
                self.balance = self.balance-amount
                print("Cash withdrawl successfully---!")
            else:
                print("Insufficinet balance")
        else:
            print("Invalid pin")
    def check_balance(self):
        temp = input("Enter your pin--!")
        if temp == self.pin:
            print("Total balance is:  " ,self.balance)
        else:
            print("Invalid pin--!")
    def exit_func(self):
        print("Thanku for using Allied Services:")
        exit()




if __name__=="__main__":
    obj = Atm()
    print(id(obj))
    obj.dospit_cash()
    obj.withdrawl_cash()
    obj.check_balance()
