from item import *
def test_item():
  orange = Item("orange", 0.50, 20)
  assertEquals(item.str(),"orange $0.50 $20")
def test_display():
  strawberry = Item("strawberry", 1.0, 25)
  milk = Item("milk", 3.25, 15)
  assertEquals(item.display(),"orange milk")
