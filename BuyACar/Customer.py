class Customer:

    def __init__(self, params):

     self.customer_id = params[0]
     self.name = params[1]
     self.address = params[2]

    #if len(params[3]) == 10:
     self.phone_number = params[3]

    #gender_list = ("M", "F")
    #if params[4] in gender_list:
     self.gender = params[4]

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

