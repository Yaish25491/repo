class Vehicle:

    def __init__(self, params):
        # for param in params:
        #    print(param)

        self.licence_plate = params[0]
        self.vehicle_type = params[1]
        self.manufacturer = params[2]
        self.model = params[3]

        params[4] = str(params[4])
        while len(params[4]) < 4:
            params[4] = "0" + params[4]
        self.year = params[4]

        params[5] = int(params[5])
        if params[5] > 3000000:
            params[5] = 3000000
        if params[5] < 1000:
            params[5] = 1000
        self.price = params[5]

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.licence_plate, self.vehicle_type, self.manufacturer,
                                               self.model,
                                               self.year, self.price)

    def __repr__(self):
        return self.__str__

    def print_me(self):
        print("licence_plate:    {}".format(self.licence_plate))
        print("vehicle_type:     {}".format(self.vehicle_type))
        print("manufacturer:     {}".format(self.manufacturer))
        print("model:            {}".format(self.model))
        print("year:             {}".format(self.year))
        print("price:            {}".format(self.price))


class CollectorsVehicle(Vehicle):

    def __init__(self, params):
        tmp = params[0:6]
        super().__init__(tmp)

        if params[6] < 0:
            params[6] = 0
        self.km = params[6]

        self.Old_Owners = int(params[7])
        self.test = tuple(list(eval(params[8])))

    def print_me(self):
        super().print_me()
        print("KM:               {}".format(self.km))
        print("Number Of Owners: {}".format(self.Old_Owners))
        print("Test Date:        {}".format(self.test))

    def __str__(self):
        back = super().__str__()
        return back + ", {}, {}, {}".format(self.km, self.Old_Owners, self.test)

    def __repr__(self):
        return self.__str__()


# def IsCollector(self):
#    is_collector = False
#   if Vehicle is CollectorsVehicle:
#      is_collector = True
# return is_collector

vehicleTest = Vehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400, 2963630, 9, "(1, 2021)"])
c = CollectorsVehicle([1155999, "Car", "Toyota", "Corolla", 2020, 83400, 2963630, 9, "(1, 2021)"])
# c.print_me()
print(c)
