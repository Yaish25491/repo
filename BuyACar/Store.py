import csv

from BuyACar.Vehicle import Vehicle
from BuyACar.Customer import Customer
from BuyACar.VIPCustomer import VIPCustomer
from BuyACar.CollectorsVehicle import CollectorsVehicle


class Store:

    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

        self.vehicles = []
        self.collectors_vehicle = []
        with open(self.vehicle) as vehicle_supply:
            vehicle_read = csv.reader(vehicle_supply)
            next(vehicle_read)
            for row in vehicle_read:
                if len(row) == 6:
                    self.vehicles.append(Vehicle(row))
                else:
                    self.collectors_vehicle.append(CollectorsVehicle(row))

        self.customers = []
        self.VIP_Customer = []
        with open(self.customer) as customers_list:
            customers_read = csv.reader(customers_list)
            next(customers_read)
            for row in customers_read:
                if len(row) == 5:
                    self.customers.append(Customer(row))
                else:
                    self.VIP_Customer.append(VIPCustomer(row))

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def get_all_collector(self):
        return self.collectors_vehicle

    def get_vehicle(self, licence_plate):

        v = None
        for vehicle in self.vehicles:
            if vehicle.licence_plate == str(licence_plate):
                v = vehicle
                break
        return v

    def get_all_by_KM_under(self, km):

        km_under = []
        for vehicle in self.collectors_vehicle:
            if vehicle.km <= int(km):
                km_under.append(vehicle)
        return km_under

    def add_vehicle(self, vehicle):
        is_added = False
        if self.get_vehicle(vehicle.licence_plate) is None:
            self.vehicles.append(vehicle)
            is_added = True

        return is_added

    def remove_vehicle(self, vehicle):

        is_removed = False
        vehicle_to_remove = self.get_vehicle(str(vehicle))
        if vehicle_to_remove is not None:
            self.vehicles.remove(vehicle_to_remove)
            is_removed = True
        return is_removed

    def get_all_by_manufacturer(self, manufacturer):
        vehicle_by_manufacturer = []
        for vehicle in self.vehicles:
            if vehicle.manufacturer == manufacturer:
                vehicle_by_manufacturer.append(vehicle)
        return vehicle_by_manufacturer

    def get_all_by_price_under(self, price):
        price_under = []
        for vehicle in self.vehicles:
            if vehicle.price < int(price):
                price_under.append(vehicle)
        return price_under

    def get_most_expansive_vehicle(self):
        most_expensive = None
        max_price = 0
        for vehicle in self.vehicles:
            if vehicle.price > max_price:
                max_price = vehicle.price
                most_expensive = vehicle
        return most_expensive

    def print_customers(self):
        for customers in self.customers:
            print(customers)

    def get_all_vip(self):
        return VIPCustomer

    def get_customer(self, customer_id):
        c = None
        for customer in self.customers:
            if customer.customer_id == str(customer_id):
                c = customer
                break
        return c

    def get_all_entitled(self):
        entitled = []
        for costumer in self.VIP_Customer:
            if costumer:
                entitled.append(costumer)
        return entitled

    def add_customer(self, customer):
        is_added = False
        if self.get_customer(customer.customer_id) is None:
            self.customers.append(customer)
            is_added = True
        return is_added

    def remove_customer(self, customer_id):
        is_removed = False
        customer_to_remove = self.get_customer(customer_id)
        if customer_to_remove is not None:
            self.customers.remove(customer_to_remove)
            is_removed = True
        return is_removed
