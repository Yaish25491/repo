class Vehicle:

    def __init__(self, params):
        self.licence_plate = params[0]
        self.vehicle_type = params[1]
        self.manufacturer = params[2]
        self.model = params[3]
        self.year = params[4]
        self.price = params[5]

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.licence_plate, self.vehicle_type, self.manufacturer, self.model,
                                           self.year)

    def __repr__(self):
        return self.__str__

    def print_me(self):
        print("licence_plate:    {}".format(self.licence_plate))
        print("vehicle_type:     {}".format(self.vehicle_type))
        print("manufacturer:     {}".format(self.manufacturer))
        print("model:            {}".format(self.model))
        print("year:             {}".format(self.year))
        print("price:            {}".format(self.price))