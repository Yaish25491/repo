from Vehicle import *


class CollectorsVehicle(Vehicle):

    def __init__(self, params):
        tmp = params[0:6]
        super().__init__(tmp)

        if int(params[6]) < 0:
            params[6] = 0
        self.km = int(params[6])

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

    def IsCollector(self):
        return True
