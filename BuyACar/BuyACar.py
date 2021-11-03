#import csv from pandas


class Vehicle:

    def __init__(self, vehicle_info):
        self.vehicle_info = vehicle_info()

    def print_me(self):
        print("-------", self.vehicle_info[0], "-------")
        print("Type:", self.vehicle_info[1])
        print("Modle", self.vehicle_info[2])
        print("Year:", self.vehicle_info[3])
        print("Price:", self.vehicle_info[4])


    """""def __init__(self, licence_plate, vehicle_type, manufacturer, model, year, price):
        self.licence_plate = licence_plate
        self.vehicle_type = vehicle_type
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.price = price
    #def __repr__(self):
      #  print()

    def print_me(self):
        print("-------", self.licence_plate, "-------")
        print("Type:", self.vehicle_type)
        print("Modle", self.model)
        print("Year:", self.year)
        print("Price:", self.price)
"""""
v = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400])

v.print_me()
