from BuyACar.ExceptionVehicle import *


class Customer:

    def __init__(self, params):
        self.customer_id = params[0]
        self.name = params[1]
        self.address = params[2]
        self.phone_number = int(params[3])
        self.gender = params[4].strip
        try:
            ExceptionProcess().CheckIntNumbers(self.phone_number, 100000000, 9999999999, "customer")
        except ExceptionVehicle as Err:
            print(Err)
            phone_number = int(self.phone_number)
            while phone_number < 1000000000:
                phone_number = phone_number*10

        gender_list = ("M", "F")
        if self.gender not in gender_list:
            self.gender = "F"

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.customer_id, self.name, self.address, self.phone_number, self.gender)

    def __repr__(self):
        return self.__str__

    def print_me(self):
        print("customer_id:    {}".format(self.customer_id))
        print("name:           {}".format(self.name))
        print("manufacturer:   {}".format(self.address))
        print("phone_number:   {}".format(self.phone_number))
        print("gender:         {}".format(self.gender))
