from item import *

def test_item():
  orange = Item("orange", 0.50, 20)
  assert orange.__str__() == "orange $0.50 20"

def test_display_name():
  strawberry = Item("strawberry", 0.70, 35)
  assert strawberry.display() == "strawberry"

