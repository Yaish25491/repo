import csv

from BuyACar.Vehicle import Vehicle
from BuyACar.Customer import Customer


class Store:

    def __int__(self,vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

        with open(self.vehicle) as vehicle_supply:
            vehicle_read = csv.reader(vehicle_supply)
            next(vehicle_read)
            for row in vehicle_read:
                Vehicle(row)

        with open(self.customer) as customers_list:
            customers_read = csv.reader(customers_list)
            next(customers_read)
            for row in customers_read:
                Customer(row)

    def print_vehicles(self):
        for row in Vehicle:
            print(row)

    def get_vehicle(self):


