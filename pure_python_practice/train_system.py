import requests
import json
class Train:
    def __init__(self):
        user_input = input(""" How would you like to proceed
        1.Enter 1 to check train live status
        2.Enter 2 to check PNR
        3.Enter 3 to check train schedule
        """)
        if user_input == "1":
            print("Train live status")
        elif user_input == "2":
            print("Check PNR")
        else:
            self.train_schedule()
    def train_schedule(self):
        train_no =input("Enter train number")
        self.fetch_data(train_no)
    def fetch_data(self,train_no):
        data  = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey "
                             "/30c382602bfa67c8a7c580e6cfe2becb/TrainNumber/{}").format(train_no)
        data = data.json()
        for i in data:
            print(i['StationName'])
obj = Train()

