# Base Class - Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived Class - Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Derived Class - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Derived Class - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Function to demonstrate polymorphism
def demonstrate_move(vehicle):
    vehicle.move()

# Example usage
car = Car()
plane = Plane()
boat = Boat()

demonstrate_move(car)    # Output: Driving 🚗
demonstrate_move(plane)  # Output: Flying ✈️
demonstrate_move(boat)   # Output: Sailing 🚤
