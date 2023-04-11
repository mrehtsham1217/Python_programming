from tylorHotel import joytyler_hotel
from tylorcustomer import joyTylor_customer
if __name__ == "__main__":
    hotel = joytyler_hotel()
    print("Ewelcome to my hotel!")
    while (True):
        print("\nChoose what you want to perform:\n")
        print("1. Checkin Customer?")
        print("2. Checkout Customer?")
        print("3. Count of Current Customers?")
        print("4. List of Current Customers?")
        print("5. Exit?\n")
        user_input = int(input("Enter choice "))
        if user_input == 1:
            new_customer = joyTylor_customer()
            new_customer.getInput()
            hotel.checkIn(new_customer)
            print("New customerd are added\n")
        elif user_input == 2:
            room_number = int(input("Please enter your pet room:\t "))
            customer_name = input("ENter your name\t")
            if hotel.checkOut(room_number, customer_name):
                print("\n Checkout done successfully :\t")
            else:
                print("Errotr in matching the details:\t")
        elif user_input == 3:
            hotel.countCustomers()
        elif user_input == 4:
            hotel.currentCustomerlist()
        elif user_input == 5:
            print("Thankuu for your visit:\t")
            break
        else:
            print("Invalid choice entered---:\t")
