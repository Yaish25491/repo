class Publication:
    def __init__(self, price, title):
        self.title = title
        self.price = price

class Book:

    pass
class Newspaper:
    pass
class Magazin:
    pass
class Periodical(Publication):
    def __init__(self,  title, price, publisher, period):
        super().__init__(price, title)
        self.publisher = publisher
        self.period = period


