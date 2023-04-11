class joytyler_hotel:
    def __init__(self):
        self.newCustomer = []

    def checkIn(self, customerRecord):
        self.newCustomer.append(customerRecord)

    def checkOut(self, pet_room_no, customer_name):
        found = False
        for customers in self.newCustomer:
            if customers.getRoomNo() == pet_room_no and customers.getname() == customer_name:
                found = True
                self.newCustomer.remove(customers)
                return found
            # count length of customers

    def countCustomers(self):
        print(f"current customers in the hotel are:{len(self.newCustomer)}")
    # printing the data

    def currentCustomerlist(self):
        print(f"Current customers are \n")
        count = 1
        for customers in self.newCustomer:
            print("\n----------------------------------------------------\n")
            print(f"Customer {count}:")
            print(customers)
            count += 1
