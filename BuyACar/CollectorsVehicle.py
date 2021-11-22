from BuyACar import Vehicle


class CollectorsVehicle(Vehicle):
    def __init__(self, params, km, old_owners, test):
        super().__init__(params)

        if km < 0:
            km = 0
            self.km = km

        self.Old_Owners = int(old_owners)
        self.test = tuple(test)

    def print_me(self):
        print("licence_plate:    {}".format(self.licence_plate))
        print("vehicle_type:     {}".format(self.vehicle_type))
        print("manufacturer:     {}".format(self.manufacturer))
        print("model:            {}".format(self.model))
        print("year:             {}".format(self.year))
        print("price:            {}".format(self.price))
        print("KM:               {}".format(self.km))
        print("Number Of Owners: {}".format(self.Old_Owners))
        print("Test Date:        {}".format(self.test))

    def __str__(self):
        back = super().__str__()
        return back + "{}, {}, {}".format(self.km, self.Old_Owners, self.test)

    def __repr__(self):
        return self.__str__()

    def IsCollector(self):
        is_collector = False
        if Vehicle is CollectorsVehicle:
            is_collector = True
        return is_collector
