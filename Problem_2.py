from building_manager import Building
import os

buildings = {}

def save_buildings_to_file():
    with open('buildings.txt', 'w') as file:
        for building in buildings.values():
            file.write(f"{building.name},{building.floor}")

def load_buildings_from_file():
    if os.path.exists('buildings.txt'):
        with open('buildings.txt', 'r') as file:
            for line in file:
                name, floor = line.strip().split(',')
                building = Building(name, floor)
                buildings[name] = building

load_buildings_from_file()


while True:
    action = input("Enter action (add, display, save, exit): ").lower()
    if action == 'exit':
        break
    
    try:
        if action == "add":
            floor = input("Enter the number of floors ")
            name = input("Enter the name of the bulidng ")
            buildings[name] = Building(name, floor)
        elif action == "display":
            for building in buildings.values():
                building.display_building()
        elif action == 'save':
            save_buildings_to_file()
            print("Buildings saved to file. ")
    except Exception as e:
        print(f"An error ocurred: {e}")

print("Building management system closed.")