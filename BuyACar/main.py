from Vehicle import Vehicle
from Customer import Customer
from Store import Store
import os


def main():
    print("#####################################################################")
    print(os.path.dirname(os.path.abspath(__file__)))
    print("#####################################################################")

    vehicleTest = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400])
    customerTest = Customer([98699, "Candace Parker", "Bates Street.St Louis", 503236702, "L"])
    AutoShopUSA = Store("vehicles_supply.csv", "customers.csv")

    print("#####################################################################")
    AutoShopUSA.print_vehicles()
    print("#####################################################################")
    AutoShopUSA.print_customers()
    print("#####################################################################")
    AutoShopUSA.add_vehicle(vehicleTest)
    print("#####################################################################")
    AutoShopUSA.add_customer(customerTest)
    print("#####################################################################")
    AutoShopUSA.remove_customer(vehicleTest)
    print("#####################################################################")
    AutoShopUSA.get_all_by_manufacturer("Kia")
    print("#####################################################################")
    AutoShopUSA.get_all_by_manufacturer("BMW")
    print("#####################################################################")
    AutoShopUSA.get_all_by_price_under("15000")
    print("#####################################################################")
    AutoShopUSA.get_most_expansive_vehicle()
    print("#####################################################################")
    AutoShopUSA.get_vehicle(25972119)
    print("#####################################################################")
    AutoShopUSA.get_customer(59769)
    print("#####################################################################")


if __name__ == "__main__":
    main()
