class Bus:
    def __init__(self, name, fare, route_num, amount_on_bus):
        self.name = name
        self.fare = fare
        self.route = route_num
        self.passenger = amount_on_bus
        self.bus_cap = 60 - amount_on_bus
    
    def information_bus(self):
        print(f"The bus for {self.name} is ${self.fare} with the route number of {self.route}. There are only {self.bus_cap} seats left! ")


city_fare = {'Chicago': 2.5, 'Bartlett': 1.5, 'Hanover Park': 2, 'Schaumburg': 2.2}

while True:
    action = input("Enter action (search, display, exit) ").lower()
    if action == 'exit':
        break
    try:
        if action == 'search':
            street_name = input("Enter the city name. ")
            if street_name in city_fare:
                r_num = input("Please enter the route number. ")
                people_on_bus = int(input("Please enter the amount of people on the bus. "))
                bus = Bus(street_name, city_fare[street_name], r_num, people_on_bus)
                bus.information_bus()
            else:
                print("The city you are looking for is not valid in the list. Make sure to capitalize the first letter!")

        elif action == 'display':
            for city in city_fare:
                print(f"The city {city} has a bus fare of {city_fare[city]}")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Not a valid choice")

print("Bus management system closed.")
