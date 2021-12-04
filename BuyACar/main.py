from Vehicle import Vehicle
from CollectorsVehicle import CollectorsVehicle
from Customer import Customer
from Store import Store

import os


def main():
    #####################################################################
    # In some casses\os the script fails to open the csv files due to path issues
    # Use this snippet as a work-arround for the issue
    # current_path = os.path.dirname(os.path.abspath(__file__))
    # vPath = os.path.join(current_path + "/" + "vehicles_supply.csv")
    # cPath = os.path.join(current_path + "/" + "customers.csv")
    # AutoShopUSA = Store(vPath, cPath)
    #####################################################################

    vehicleTest = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400])
    customerTest = Customer([98699, "Candace Parker", "Bates Street.St Louis", 503236702, "L"])
    AutoShopUSA = Store("vehicles.csv", "customers.csv")
    vehicleTest = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400, 2963630, 9, "(1, 2021)"])
    c = CollectorsVehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400, 2963630, 9, "(1, 2021)"])
    c.print_me()
    print(c)

"""""
    print("######################### ALL Vehicles #################################")
    AutoShopUSA.print_vehicles()
    print("######################### All Costumers ##############################")
    AutoShopUSA.print_customers()
    print("######################### Add Vehicle ##############################")
    print(AutoShopUSA.add_vehicle(vehicleTest))
    print("######################### Add Costumers ###############################")
    print(AutoShopUSA.add_customer(customerTest))
    print("######################### Remove Costumer ##############################")
    print(AutoShopUSA.remove_customer(53374408))
    print("######################### All by Manufacturer #############################")
    vehicle_by_manufacturer = AutoShopUSA.get_all_by_manufacturer("Kia")
    for vehicle in vehicle_by_manufacturer:
        print(vehicle)
    print("######################### All by Under Price ###########################")
    price_under = AutoShopUSA.get_all_by_price_under("15000")
    for vehicle in price_under:
        print(vehicle)
    print("######################### Most Expansive ############################")
    print(AutoShopUSA.get_most_expansive_vehicle())
    print("######################### Get Vehicle ##############################")
    print(AutoShopUSA.get_vehicle(46132049))
    print("######################### Get Costumer ###############################")
    print(AutoShopUSA.get_customer(59769))
    print("#####################################################################")
"""

if __name__ == "__main__":
    main()
