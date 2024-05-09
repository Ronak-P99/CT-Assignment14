class Building:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor  

    def display_building(self):
        print(f"Building: {self.name}, Floors: {self.floor}")
