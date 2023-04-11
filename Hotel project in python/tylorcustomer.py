class joyTylor_customer:
    # delcartion of class
    # constructor
    def __init__(self, name="Default", customer_type="Default", size_of_room="Default", length_of_stay=0, roomNo=0):
        self.__name = name
        self.__customer_type = customer_type
        self.__size_of_room = size_of_room
        self.__length_of_stay = length_of_stay
        self.__roomNo = roomNo
    # getter for this class

    def getname(self):
        return self.__name

    def getCustomer_type(self):
        return self.__customer_type

    def getSize_of_room(self):
        return self.__size_of_room

    def getlength_of_stay(self):
        return self.__length_of_stay

    def getRoomNo(self):
        return self.__roomNo
    # setter for this  class

    def setname(self, name):
        self.__name = name

    def setcustomer_type(self, customer_type):
        self.__customer_type = customer_type

    def SetSize_of_room(self, size_of_room):
        self.__size_of_room = size_of_room

    def SetLength_of_stay(self, length_of_stay):
        self.__length_of_stay = length_of_stay

    def setRoom(self, roomNo):
        self.__roomNo = roomNo
    # tostring method in python
    # purose: This mostly represent the string representation of an object

    def __str__(self):
        to_return = ""
        to_return = f"Name:\t{self.__name}\n"
        to_return = f"Name:\t{self.__customer_type}\n"
        to_return = f"Name:\t{self.__size_of_room}\n"
        to_return = f"Name:\t{self.__length_of_stay}\n"
        to_return = f"Name:\t{self.__roomNo}\n"
        return to_return
    # getting input from user using setter functions

    def getInput(self):
        self.setname(input("Enter the name of customer:\t"))
        self.setcustomer_type(input("dog cat goat etc ,-----\t"))
        self.SetSize_of_room(
            input("Enter the size of room ---small, medium and large\t"))
        self.SetLength_of_stay(int(input("How many days you want to stay\t")))
        self.setRoom(int(input("Enter the room no.\t")))
