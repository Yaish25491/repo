from Vehicle import Vehicle
from CollectorsVehicle import CollectorsVehicle
from Customer import Customer
from Store import Store
from VIPCustomer import VIPCustomer
import os
import GUI
from BuyACar.ExceptionVehicle import *
from tkinter import *

def main():
    #####################################################################
    # In some casses\os the script fails to open the csv files due to path issues
    # Use this snippet as a work-arround for the issue
    # current_path = os.path.dirname(os.path.abspath(__file__))
    # vPath = os.path.join(current_path + "/" + "vehicles_supply.csv")
    # cPath = os.path.join(current_path + "/" + "customers.csv")
    # AutoShopUSA = Store(vPath, cPath)
    #####################################################################

    try:
        window = Tk()
        window.title("AutoShopUSA")
        window.geometry('700x400')
        lbl = Label(window, text="AutoShopUSA", font=("d Bold", 25))
        lbl.grid(column=3, row=1)
        AutoShopUSA = Store("vehicles.csv", "customers.csv")
        vehicleTest = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400])
        customerTest = Customer([98699, "Candace Parker", "Bates Street.St Louis", 503236702, "L"])




        print("######################### ALL Vehicles #################################")

        def get_vic():
            AutoShopUSA.print_vehicles()

        print_vehicles_but = Button(window, text="print_vehicles", command=get_vic())
        print_vehicles_but.grid(column=4, row=3)

        print("######################### ALL Collectors Vehicles #################################")

        def get_collectors():
            collectors_list = AutoShopUSA.collectors_vehicle
            for vehicle in collectors_list:
                print(vehicle)

        get_all_collector_but = Button(window, text="get_all_collector", command=get_collectors())
        get_all_collector_but.grid(column=2, row=2)

        print("######################### get all by KM under ##############################")

        def print_by_KM():
            data = int(txt3.get())
            AutoShopUSA.get_all_by_KM_under(data)

        but15 = Button(window, text="Print all vehicle under KM", width=35, command=print_by_KM)
        but15.grid(column=3, row=4)
        txt3 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt3.insert(0, "KM")
        txt3.grid(column=3, row=5)

    #    for vehicle in AutoShopUSA.get_all_by_KM_under(15000):
    #        print(vehicle)
        print("######################### All VIP Costumers ##############################")

        def get_vip():
            VIPlist = AutoShopUSA.VIP_Customer
            for costumer in VIPlist:
                print(costumer)

        get_all_vip_but = Button(window, text="get_all_vip", command=get_vip())
        get_all_vip_but.grid(column=3, row=2)

        print("######################### All Entitled ##############################")

        def get_entitled():
            for costumer in AutoShopUSA.get_all_entitled():
                print(costumer)
        get_all_entitled_but = Button(window, text="All Entitled", command=get_entitled())
        get_all_entitled_but.grid(column=4, row=2)

        print("######################### All Costumers ##############################")

        def all_costumers():
            AutoShopUSA.print_customers()
        print_customers_but = Button(window, text="print_customers", command=all_costumers())
        print_customers_but.grid(column=2, row=3)

        print("######################### Add Vehicle ##############################")

        def add_via():
            data = ([int(txt1_7.get()), txt2_7.get().capitalize(), txt3_7.get().capitalize(),
                     txt4_7.get(), int(txt5_7.get()), int(txt6_7.get())])
            AutoShopUSA.add_vehicle(data)

        but8 = Button(window, text="add vehicle", width=30, command=add_via)
        but8.grid(column=2, row=4)

        txt1_7 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt1_7.insert(0, "licence plate")
        txt2_7 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt2_7.insert(0, "type")
        txt3_7 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt3_7.insert(0, "manufacturer")
        txt4_7 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt4_7.insert(0, "model")
        txt5_7 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt5_7.insert(0, "year")
        txt6_7 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt6_7.insert(0, "price")

        txt1_7.grid(column=2, row=5)
        txt2_7.grid(column=2, row=6)
        txt3_7.grid(column=2, row=7)
        txt4_7.grid(column=2, row=8)
        txt5_7.grid(column=2, row=9)
        txt6_7.grid(column=2, row=10)
#        print(AutoShopUSA.add_vehicle(vehicleTest))
        print("######################### Add Costumers ###############################")

        def add_cus():
            data = (
            [int(txt1_5.get()), txt2_5.get().capitalize(), txt3_5.get().capitalize(), txt4_5.get(), txt5_5.get()])
            AutoShopUSA.add_customer(data)

        but6 = Button(window, text="add customer", width=30, command=add_cus)
        but6.grid(column=4, row=4)

        txt1_5 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt1_5.insert(0, "id number")
        txt2_5 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt2_5.insert(0, "name")
        txt3_5 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt3_5.insert(0, "address")
        txt4_5 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt4_5.insert(0, "phone")
        txt5_5 = Entry(window, width=15, font=('david', 10, 'bold'))
        txt5_5.insert(0, "gender")

        txt1_5.grid(column=4, row=5)
        txt2_5.grid(column=4, row=6)
        txt3_5.grid(column=4, row=7)
        txt4_5.grid(column=4, row=8)
        txt5_5.grid(column=4, row=9)
#        print(AutoShopUSA.add_customer(customerTest))
        print("######################### Remove Costumer ##############################")

        remove_cus_txt = Entry(window, width=15, font=('david', 10, 'bold'))
        remove_cus_txt.insert(0, "id number")
        remove_cus_txt.grid(column=2, row=13)

        def remove_cus():

            data = int(remove_cus_txt.get())
            AutoShopUSA.remove_customer(data)

        remove_cus_but = Button(window, text="remove customer", width=30, command=remove_cus)
        remove_cus_but.grid(column=2, row=12)

        print("######################### All by Manufacturer #############################")
        get_all_by_manufacturer_txt = Entry(window, width=15)
        get_all_by_manufacturer_txt.insert(0, "Manufacturer")
        get_all_by_manufacturer_txt.grid(column=4, row=13)
        get_all_by_manufacturer_txt.focus()

        def print_by_manu():
            data = get_all_by_manufacturer_txt.get().capitalize()
            AutoShopUSA.get_all_by_manufacturer(data)
            get_all_by_manufacturer_but = Button(window, text="print by manufacturer", width=30, command=print_by_manu)
            get_all_by_manufacturer_but.grid(column=4, row=12)

#        vehicle_by_manufacturer = AutoShopUSA.get_all_by_manufacturer("Kia")
#        for vehicle in vehicle_by_manufacturer:
#            print(vehicle)
        print("######################### All by Under Price ###########################")
        get_all_by_price_under_txt = Entry(window, width=10)
        get_all_by_price_under_txt.insert(0, "Price")
        get_all_by_price_under_txt.grid(column=2, row=15)
        get_all_by_price_under_txt.focus()

        def print_under():
            data = int(txt6_7.get())
            AutoShopUSA.get_all_by_under(data)

        get_all_by_price_under = Button(window, text="get_all_by_price_under", width=30, command=print_under)
        get_all_by_price_under.grid(column=2, row=14)

#        price_under = AutoShopUSA.get_all_by_price_under("15000")
#       for vehicle in price_under:
#            print(vehicle)
        print("######################### Most Expansive ############################")

        def most_exp():
            print(AutoShopUSA.get_most_expansive_vehicle())

        get_most_expansive_vehicle_but = Button(window, text="get_most_expansive_vehicle", command=most_exp())
        get_most_expansive_vehicle_but.grid(column=3, row=3)

        print("######################### Get Vehicle ##############################")

        get_vehicle_txt = Entry(window, width=10)
        get_vehicle_txt.grid(column=4, row=15)
        get_vehicle_txt.focus()
        def get_vehi():
            data = int(get_vehicle_txt.get())
            AutoShopUSA.get_vehicle(data)
        but13 = Button(window, text="print vehicle by LP ", width=30, command=get_vehi)
        but13.grid(column=4, row=14)

            #print(AutoShopUSA.get_vehicle(46132049))
        print("######################### Get Costumer ###############################")
        get_customer_txt = Entry(window, width=10)
        get_customer_txt.grid(column=3, row=13)
        get_customer_txt.focus()

        def print_by_id():
            data = int(get_customer_txt.get())
            AutoShopUSA.get_customer(data)

        but13 = Button(window, text="print customer by id ", width=30, command=print_by_id)
        but13.grid(column=3, row=12)
#        print(AutoShopUSA.get_customer(59769))
        print("#####################################################################")

        window.mainloop()

    except ExceptionVehicle as Err:
        print(Err)

    else:
        print("Program finished with success")

if __name__ == "__main__":
    main()
