import distutils

from Customer import *


class VIPCustomer(Customer):

    def __init__(self, params):
        tmp = params[0:5]
        super().__init__(tmp)

        self.StartDate = tuple(list(eval(params[5])))
        self.BirthDate = tuple(list(eval(params[6])))
        self.JoiningPresent = params[7] == 'True'

    def __str__(self):
        back = super().__str__()
        return back + ", {}, {}, {}".format(self.StartDate, self.BirthDate, self.JoiningPresent)

    def __repr__(self):
        return self.__str__()

    def GetPresent(self):
        if self.JoiningPresent == True:
            print("Congratulations here is your present")
            self.JoiningPresent = False
        else:
            print("You already got your present")
