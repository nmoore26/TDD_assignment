class Item:
  def __init__(self,name,price,count):
    self.name = name
    self.price = price
    self.count = count
  def __str__(self):
    print(f'{name} ${price} {count}')
