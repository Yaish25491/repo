
class Cars:
    def __init__(self, id, speed):
        self.id = id
        self.speed = speed
    def __str__(self):
        back = "The speed of car number " + str(self.id) + " is " + str(self.speed)
        return back

    def print_car(self):
        print("The speed of car number", self.id, "is", self.speed)

    def accelerate(self, speed_change):
        speed = int(self.speed)
        change = int(speed_change)
        new_speed = speed + change
        print(new_speed)
    def decelerate(self):
        speed = int(self.speed)
        new_speed = speed -2
        print(new_speed)

car1 = Cars("574693","60")
car2 = Cars("976576", "0")
car1.print_car()
print("*********************")
car1.accelerate("20")
print("*********************")
car1.decelerate()

print(car1)
print(car2)

