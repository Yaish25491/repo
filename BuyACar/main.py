from Vehicle import Vehicle
from Customer import Customer
from Store import Store
import os



def main():
    print("#####################################################################")

    print(os.path.dirname(os.path.abspath( __file__ )))
    print("#####################################################################")

    v = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400])
    print("#####################################################################")
    #v.print_me()
    print("#####################################################################")
    #print(v)
    print("#####################################################################")

    c = Customer([98699, "Candace Parker", "Bates Street.St Louis", 503236702, "L"])
    print("#####################################################################")
    #c.print_me()
    print("#####################################################################")
    #print(c)
    print("#####################################################################")


    s = Store("vehicles_supply.csv", "customers.csv")


if __name__ == "__main__":
    main()
