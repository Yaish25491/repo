class ExceptionVehicle(Exception):

    def __init__(self, message, level, source):
        self.message = str(message)
        self.level = int(level)
        self.source = str(source)

    def __str__(self):
        return "{} is empty, Level of severity is {}, source object: {}".format(self.message, self.level, self.source)

    def __repr__(self):
        return self.__str__()


class ExceptionProcess:

    def __init__(self):
        pass

    def CheckIntNumbers(self, var, minimum, maximum, source):

        raise_exception = False
        level = -1

        if type(var) is not int:
            raise_exception = True
            level = 9
        else:
            if not minimum is None and var < minimum:
                raise_exception = True
                level = 4

            elif not maximum is None and var > maximum:
                raise_exception = True
                level = 5

        if raise_exception:
            raise ExceptionVehicle(var, level, source)

    def CheckSTR(self, var, source):
        raise_exception = False
        level = -1

        if type(var) is not str:
            raise_exception = True
            level = 3

        elif var == "":
            raise_exception = True
            level = 3

        if raise_exception:
            raise ExceptionVehicle(var, level, source)

    def CheckList(self, var, source):
        raise_exception = False
        level = -1

        if type(var) is not list:
            raise_exception = True
            level = 2

        elif len(var) == 0:
            raise_exception = True
            level = 1

        if raise_exception:
            raise ExceptionVehicle(var, level, source)

    def CheckDic(self, var, source):
        raise_exception = False
        level = -1

        if type(var) is not dict:
            raise_exception = True
            level = 2
        elif len(var) == 0:
            raise_exception = True
            level = 1
        if raise_exception:
            raise ExceptionVehicle(var, level, source)

    def CheckTup(self, var, source):
        raise_exception = False
        level = -1

        if type(var) is not tuple:
            raise_exception = True
            level = 2
        elif len(var) == 0:
            raise_exception = True
            level = 1
        if raise_exception:
            raise ExceptionVehicle(var, level, source)
