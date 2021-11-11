import csv

from BuyACar.Vehicle import Vehicle
from BuyACar.Customer import Customer


class Store:

    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

        self.vehicles = []
        with open(self.vehicle, 'r') as vehicle_supply:
            vehicle_read = csv.reader(vehicle_supply)
            next(vehicle_read)
            for row in vehicle_read:
                self.vehicles.append(Vehicle(row))
        for v in self.vehicles:
            print(v)

        with open(self.customer) as customers_list:
            customers_read = csv.reader(customers_list)
            next(customers_read)
            for row in customers_read:
                Customer(row)

    def print_vehicles(self):
        for row in Vehicle:
            print(row)

    def get_vehicle(self):
        "getting licence plate and returning the vehicle"

    def add_vehicle(self):
        "getting vehicle object, checking if exist, if not adding"

    def remove_vehicle(self):
        "getting vehicle object, checking if exist, if yes removing"

    def get_all_by_manufacturer(self):
        "getting manufacturer and returning a list of matching vehicles  "

    #def get_all_by_price_under(self):

   #def get_most_expansive_vehicle(self):



