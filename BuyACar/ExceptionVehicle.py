class ExceptionVehicle:

    def __init__(self, message, level, source):
        self.message = str(message)
        self.level = int(level)
        self.source = str(source)

    def __str__(self):
        return "{} is empty, Level of severity is {}, source object: {}".format(self.message, self.level, self.source)

    def __repr__(self):
        return self.__str__()


x = ExceptionVehicle("r", 3, "t")
print(x)


class ExceptionProcess:

    def __init__(self):
        pass

    def ChecklntNumbers(self, var, minimum, maximum, source):
        self.var = var
        self.minimume = int(minimum)
        self.maximum = int(maximum)
        self.source = source

        try:
          if self.var is not int:

              raise ExceptionVehicle(self.var, 5, self.source)

        try:
            if self.var < self.minimume:
                if self.var > self.maximum:

                raise ExceptionVehicle(self.var, 4, self.source)

d = ExceptionProcess.ChecklntNumbers("d",3,8,"Vehicles")
print(d)