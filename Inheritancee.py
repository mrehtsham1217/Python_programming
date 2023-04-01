class Employee:
    def __init__(self, E_Name, E_ID):
        self._E_Name = E_Name
        self._E_ID = E_ID


class Manager(Employee):
    def __init__(self, _E_Name, _E_ID, E_Designation):
        super().__init__(_E_Name, _E_ID)
        self.E_Designation = E_Designation

    def printinfo(self):
        print(
            f"Name {self.E_Name} \nID{self.E_ID}\n designation is {self.E_Designation}")


obj = Manager("Ehtsham", 1217, "Manager")
obj.printinfo()

# ---------------declare private members in class----------------------

# class Account:
#     def __init__(self, amount, name):
#         self.__amount = amount
#         self.__name = name

#     def printInfo(self):
#         print(f"Amount:{self.__amount}, Name:{self.__name}")


# user = Account(200000, "Fatima")
# user.printInfo()
