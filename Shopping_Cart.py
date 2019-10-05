class ShoppingCart(object):
  def __init__(self):
    self.total=0
    self.items={}
  def add_item(self, item_name, quantity, price):
    self.total =self.total+(price*quantity)
    self.items[item_name]=quantity
  def remove_item(self, item_name, quantity, price):
    if quantity < self.items[item_name]:
      self.total=self.total-(price * quantity)
      self.items[item_name]=self.items[item_name]-quantity
    else:
      self.total=self.total-(self.items[item_name]*price)
      del self.items[item_name]
  def checkout(self, cash_paid):
    if cash_paid<self.total:
      return "Cash paid not enough"
    return cash_paid-self.total
    
class Shop(ShoppingCart):
  def __init__(self):
    self.quantity=100
  def remove_item(self, *args):
    try:
      args[0]
    except:
      self.quantity-=1
    
        
