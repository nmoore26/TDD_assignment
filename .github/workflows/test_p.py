from item.py import *

def test_item():
  orange = Item("orange", 0.50, 20)
  assert str(orange) == "orange $0.50 20"

def test_display():
  strawberry = Item("strawberry", 0.70, 35)
  assert strawberry.display() == "strawberry"

