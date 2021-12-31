class ExceptionVehicle:

    def __init__(self, message, level, source):
        self.message = str(message)
        self.level = int(level)
        self.source = str(source)

    def __str__(self):
        return "{} is empty, Level of severity is {}, source object: {}".format(self.message, self.level, self.source)

    def __repr__(self):
        return self.__str__()

x = ExceptionVehicle("r",3,"t")
print(x)

class ExceptionProcess:

