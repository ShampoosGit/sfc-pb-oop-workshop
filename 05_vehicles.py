"""
You are tasked with developing a system to manage different types of vehicles.
The system should include various types of vehicles such as cars, trucks, and motorcycles.
Each type of vehicle shares some common attributes but also has specific attributes
  and behaviors unique to its type.
You will need multiple classes to accomplish this,
  with some classes inheriting from a parent class.
See example:

car = Car("Toyota", "Corolla", 2020, 4)
truck = Truck("Ford", "F-150", 2018, 10000)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019, "Cruiser")

print(car.get_info())         # Prints car information
print(truck.get_info())       # Prints truck information
print(motorcycle.get_info())  # Prints motorcycle information


Once your classes are complete, copy and paste the above example below them in order to test their functionality.
"""

"""
Write a class that meets these requirements.

Name:       Vehicle

Required state:
   * make, the manufacturer of the vehicle
   * model, the model of the vehicle
   * year, the year the vehicle was manufactured

Behavior:
   * get_info()     # Returns information about the vehicle

"""

"""
Write a class that meets these requirements.

Name:       Car (inherits from Vehicle)

Required state:
   * doors, the number of doors on the car

Behavior:
   * get_info()     # Returns information about the car, including the number of doors

Example:
   car = Car("Toyota", "Corolla", 2020, 4)

   print(car.get_info())    # Prints car information

"""

"""
Write a class that meets these requirements.

Name:       Truck (inherits from Vehicle)

Required state:
   * towing capacity, the towing capacity of the truck in pounds

Behavior:
   * get_info()     # Returns information about the truck, including the towing capacity

Example:
   truck = Truck("Ford", "F-150", 2018, 10000)

   print(truck.get_info())    # Prints truck information

"""

"""
Write a class that meets these requirements.

Name:       Motorcycle (inherits from Vehicle)

Required state:
   * type, the type of motorcycle (e.g., cruiser, sport)

Behavior:
   * get_info()     # Returns information about the motorcycle, including the type

Example:
   motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019, "Cruiser")

   print(motorcycle.get_info())    # Prints motorcycle information

"""
class Vehicle:
   def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

   def get_info(self):
      return (f"{self.make} {self.model}, Year: {self.year}")

class Car(Vehicle):
   def __init__(self, make, model, year, doors):
      super().__init__(make, model, year)
      self.doors = doors

   def get_info(self):
      basic_info = super().get_info()
      return f"{basic_info}, Doors: {self.doors}"

class Truck(Vehicle):
   def __init__(self, make, model, year, towing_capacity):
      super().__init__(make, model, year)
      self.towing_capacity = towing_capacity

   def get_info(self):
      basic_info = super().get_info()
      return f"{basic_info}, Towing Capacity: {self.towing_capacity}"

class Motorcycle(Vehicle):
   def __init__(self, make, model, year, type):
      super().__init__(make, model, year)
      self.type = type

   def get_info(self):
      basic_info = super().get_info()
      return f"{basic_info}, Type: {self.type}"

if __name__ == "__main__":
   car = Car("Toyota", "Corolla", 2020, 4)
   truck = Truck("Ford", "F-150", 2018, 10000)
   motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019, "Cruiser")

   print(car.get_info())         # Prints car information
   print(truck.get_info())       # Prints truck information
   print(motorcycle.get_info())  # Prints motorcycle information