class Customer:

    def __init__(self, params):
        self.customer_id = params[0]
        self.name = params[1]
        self.address = params[2]

        count = 0
        while params[3] != 0:
            params[3] //= 10
            count += 1
        print(count)
        self.phone_number = params[3]
        self.gender = params[4]
        gender = self.gender
        gender_list = ("M", "F")
        if gender in gender_list:
            print("ok")
        else:
            print("notOK")
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

