#Task 1

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self):
        print(f"The new owner is {self.owner}")

#Task 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = 0

    
    def add_participant(self):
        print("A new participant has been added!")

    
    def get_participant_count(self, int):
        print(f"The total number of participants is {int}")
#Task 1  

participants = []
owner1 = Vehicle(43, "boss", "Phil")
owner2 = Vehicle(44, "boss", "Bill")

owner1.update_owner()
owner2.update_owner()

#Task 2

participant1 = Event("Ron", "10/12")
participant1.add_participant()
participants.append(participant1)
participant1.get_participant_count(len(participants))
participant2 = Event("Rick", "10/13")
participant2.add_participant()
participants.append(participant2)
participant2.get_participant_count(len(participants))

