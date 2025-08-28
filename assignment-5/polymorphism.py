# Parent Class
class Vehicle:
    def move(self):
        # This method will be overridden by child classes
        pass


# Child Class 1
class Car(Vehicle):
    def move(self):
        print("Driving on the road!")


# Child Class 2
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")


# Child Class 3
class Bike(Vehicle):
    def move(self):
        print("Riding on the path!")


# Usage
vehicles = [Car(), Plane(), Bike()]

for v in vehicles:
    v.move()   # Polymorphism in action
