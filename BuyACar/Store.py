import csv

from BuyACar.Vehicle import Vehicle
from BuyACar.Customer import Customer


class Store:

    def __init__(self, vehicle, customer):
        self.vehicle = vehicle
        self.customer = customer

        self.vehicles = []
        with open(self.vehicle) as vehicle_supply:
            vehicle_read = csv.reader(vehicle_supply)
            next(vehicle_read)
            for row in vehicle_read:
                self.vehicles.append(Vehicle(row))
        for v in self.vehicles:
            print(v)

        self.customers = []
        with open(self.customer) as customers_list:
            customers_read = csv.reader(customers_list)
            next(customers_read)
            for row in customers_read:
                self.customers.append(Customer(row))

    def print_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def get_vehicle(self, licence_plate):
        v = None
        for vehicle in self.vehicles:
            if vehicle.licence_plate == licence_plate:
                v = vehicle
                break
        return v

    def add_vehicle(self, vehicle):
        is_added = False
        if self.get_vehicle(vehicle.licence_plate) is None:
            self.vehicles.append(vehicle)
            is_added = True

        return is_added

    def remove_vehicle(self, vehicle):
        is_removed = False
        if self.get_vehicle(vehicle.licence_plate) is not None:
            self.vehicles.remove(vehicle)
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
            if vehicle.price < price:
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

    def get_customer(self, customer_id):
        c = None
        for customer in self.customers:
            if customer.customer_id == customer_id:
                c = customer
                break
        return c

    def add_customer(self, customer):
        is_added = False
        if self.get_customer(customer.customer_id) is None:
            self.customer.append(customer)
            is_added = True
        return is_added

    def remove_customer(self, customer):
        is_removed = False
        if self.get_customer(customer.customer_id) is not None:
            self.customer.remove(customer)
            is_removed = True
        return is_removed

