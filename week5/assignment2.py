# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child classes with different move() behaviors
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"


# ------------------------
# Example usage:

vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    print(vehicle.move())
