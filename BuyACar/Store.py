import csv

from BuyACar.Vehicle import Vehicle
from BuyACar.Customer import Customer


class Store:

    with open("vehicle_supply.csv") as vehicle_supply:
        vehicle_read = csv.reader(vehicle_supply)

        next(vehicle_read)
        for row in vehicle_read:
            Vehicle(row)

    with open("customers.csv") as customers_list:
        customers = csv.reader(customers_list)

        next(customers_read)
        for row in customers_read:
            Customer(row)

    def __init__(self):