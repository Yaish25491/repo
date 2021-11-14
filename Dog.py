class Dog:
    def __init__(self,name,breed,age,id):
        self.name = name
        self.breed = breed
        self.age = age
        self.id = id
        self.dan_list = None


    def speak(self, word):
        print(word)

    def print_me(self):
        print(self.name + " is bread "+self.breed)

    def __str__(self):
        return self.name + " is bread "+self.breed

    def get_danger_breed(self, dan_list):
        self.dan_list = dan_list

    def is_danger(self):
       return self.breed in self.dan_list







dan_list = ("Wolf","Pitball")
d=Dog("d","mili",3,5)
d.speak("HAV_HAV")
d.print_me()
print(d)
print("*************")
d.get_danger_breed(dan_list)
print(d.dan_list)
print(d.is_danger())