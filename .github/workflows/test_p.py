from item import *

def test_item():
  orange = Item("orange", 0.50, 20)
  assert orange.__str__() == "orange $0.50 20"
