from Customer import Customer
from Store import Store
from Vehicle import Vehicle
from tkinter import *

store = None


def set_store(i_store):
    global store
    store = i_store


# class Store_GUI:

#   def __init__(self, store):
#      self.store = store
def run_GUI(store):
    window = Tk()
    window.title("AutoShopUSA")
    window.geometry('500x300')
    #window.config(bg='black')

    lbl = Label(window, text="AutoShopUSA", font=("d Bold", 25))
    lbl.grid(column=2, row=1)

    #bg = PhotoImage(file="pngtree-usa-flag-transparent-with-fabric-png-image_5313205.jpeg")

    #canvas1 = Canvas(window, width=400,height=400)
    #canvas1.pack(fill = "both", expand = True)

    #canvas1.create_image(0, 0, image=bg, anchor="nw")

    #label = Label(window, image=bg)
    #label.place(x=0, y=0)



    print_vehicles_but = Button(window, text="print_vehicles", command=store.print_vehicles())
    print_vehicles_but.grid(column=1, row=3)
#    print_vehicles_but.pack()

    get_all_collector_but = Button(window, text="get_all_collector", command=store.get_all_collector())
    get_all_collector_but.grid(column=1, row=5)

    get_most_expansive_vehicle_but = Button(window, text="get_most_expansive_vehicle", command=store.get_most_expansive_vehicle())
    get_most_expansive_vehicle_but.grid(column=1, row=7)

    print_customers_but = Button(window, text="print_customers", command=store.print_customers())
    print_customers_but.grid(column=1, row=9)

    get_all_vip_but = Button(window, text="get_all_vip", command=store.get_all_vip())
    get_all_vip_but.grid(column=1, row=11)

    get_all_entitled_but = Button(window, text="print_customers", command=store.get_all_entitled())
    get_all_entitled_but.grid(column=1, row=13)

    # get vehicle
    get_vehicle_txt = Entry(window, width=10)
    get_vehicle_txt.grid(column=3, row=3)
    get_vehicle_txt.focus()

    get_vehicle_but = Button(window, text="get_vehicle", command=store.get_vehicle(licence_plate=get_vehicle_txt))
    get_vehicle_but.grid(column=2, row=3)
    get_vehicle_txt = Entry(window, width=10)
    get_vehicle_txt.grid(column=3, row=3)
    get_vehicle_txt.focus()

    # get_all_by_KM_under
#    get_all_by_KM_under_txt = Entry(window, width=10)
#    get_all_by_KM_under_txt.grid(column=3, row=5)
#    get_all_by_KM_under_txt.focus()
    get_all_by_KM_under_txt = 150000
    get_all_by_KM_under = Button(window, text="get_all_by_KM_under", command=store.get_all_by_KM_under(km=get_all_by_KM_under_txt))
    get_all_by_KM_under.grid(column=2, row=5)
    get_all_by_KM_under_txt = Entry(window, width=10)
    get_all_by_KM_under_txt.grid(column=3, row=5)
    get_all_by_KM_under_txt.focus()

    # get_all_by_manufacturer
    get_all_by_manufacturer_txt = Entry(window, width=10)
    get_all_by_manufacturer_txt.grid(column=3, row=7)
    get_all_by_manufacturer_txt.focus()

    get_all_by_manufacturer = Button(window, text="get_all_by_manufacturer", command=store.get_all_by_manufacturer(manufacturer=get_all_by_manufacturer_txt))
    get_all_by_manufacturer.grid(column=2, row=7)
    get_all_by_manufacturer_txt = Entry(window, width=10)
    get_all_by_manufacturer_txt.grid(column=3, row=5)
    get_all_by_manufacturer_txt.focus()

    # get_all_by_price_under
#    price_under_txt = Entry(window, width=10)
#    price_under_txt.grid(column=3, row=5)
#    price_under_txt.focus()
    price_under_txt = 3216954
    get_all_by_price_under = Button(window, text="get_all_by_price_under", command=store.get_all_by_price_under(price=price_under_txt))
    get_all_by_price_under.grid(column=2, row=9)
    get_all_by_price_under_txt = Entry(window, width=10)
    get_all_by_price_under_txt.grid(column=3, row=9)
    get_all_by_price_under_txt.focus()

    # get_customer
    #    get_customer_txt = Entry(window, width=10)
    #    get_customer.grid(column=3, row=5)
    #    get_customer_txt.focus()
    get_customer_txt = 3216954
    get_customer = Button(window, text="get_customer", command=store.get_customer(customer_id=get_customer_txt))
    get_customer.grid(column=2, row=11)
    get_customer_txt = Entry(window, width=10)
    get_customer_txt.grid(column=3, row=11)
    get_customer_txt.focus()

    #########

    window.mainloop()
