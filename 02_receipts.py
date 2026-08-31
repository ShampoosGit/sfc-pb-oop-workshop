"""
You are tasked with developing a system to manage shopping receipts.
The system should allow for adding items to a receipt, calculating subtotals,
and applying tax rates to get the total amount due.
You will need multiple classes in order to accomplish this and one will utilize the other when being invoked.
See example:

receipt = Receipt(.1)
receipt.add_item(ReceiptItem(4, 2.50))
receipt.add_item(ReceiptItem(2, 5.00))

print(receipt.get_subtotal())     # Prints 20
print(receipt.get_total())        # Prints 22


Once your classes are complete, copy and paste the above example below them in order to test their functionality
"""


"""
Write a class that meets these requirements.

Name:       Receipt

Required state:
   * tax rate, the percentage tax that should be applied to the total

Behavior:
   * add_item(item)   # Add a ReceiptItem to the Receipt
   * get_subtotal()   # Returns the total of all of the receipt items
   * get_total()      # Multiplies the subtotal by the 1 + tax rate

"""

"""
Write a class that meets these requirements.

Name:       ReceiptItem

Required state:
   * quantity, the amount of the item bought
   * price, the amount each one of the things cost

Behavior:
   * get_total()          # Returns the quantity * price

Example:
   item = ReceiptItem(10, 3.45)

   print(item.get_total())    # Prints 34.5

"""

class Reciept():
   def __init__(self, tax_rate, items=None):
      self.tax_rate = tax_rate
      self.items = items if items is not None else []

   def add_item(self, item):
      self.items.append(item)

   def get_subtotal(self):
      return sum(item.get_total() for item in self.items)

   def get_total(self):
      return self.get_subtotal() * (1 + self.tax_rate)

class RecieptItem:
   def __init__(self, quantity, price):
      self.quantity = quantity
      self.price = price

   def get_total(self):
      return self.quantity * self.price

if __name__ == "__main__":
   receipt = Reciept(.1)
   receipt.add_item(RecieptItem(4, 2.50))
   receipt.add_item(RecieptItem(2, 5.00))

   print(receipt.get_subtotal())     # Prints 20
   print(receipt.get_total())        # Prints 22