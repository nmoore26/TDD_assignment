class Item:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return f"{self.name} ${self.price} {self.count}"

    def display(self):
        return self.name

