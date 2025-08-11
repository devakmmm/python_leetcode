class Vehicle:
    def __init__(self,make, model):
        self.make = make
        self.model = model
        
    def moves(self): #refer to itself
        print("The vehicle moves")

    def get_make_and_model(self):
        print( f"{self.make} {self.model}")
    
# Create an instance of the Vehicle class

mycar = Vehicle('Toyota', 'Corolla')
print(mycar.make)  # Output: Toyota
print(mycar.model)  # Output: Corolla   
mycar.moves()  # Output: The vehicle moves
# This code defines a simple class named Vehicle with a method moves that prints a message when called.
# An instance of the Vehicle class is created and the moves method is invoked, demonstrating basic class and method usage in Python.

mycar.get_make_and_model()  # Output: Toyota Corolla
# This code defines a method get_make_and_model within the Vehicle class that prints


class Airplane(Vehicle): #inheritance
    def moves(self):
        print("The airplane flies")

class Boat(Vehicle): #inheritance
    def moves(self):
        print("The boat sails")

class golfcart(Vehicle): #inheritance
    pass

        
myplane = Airplane("Boeing", "747")
myboat = Boat("Yamaha", "242X")
mygolfcart = golfcart("Club Car", "Precedent")

myplane.get_make_and_model()  # Output: Boeing 747
myplane.moves()  # Output: The airplane flies

myboat.get_make_and_model()  # Output: Yamaha 242X
myboat.moves()  # Output: The boat sails

mygolfcart.get_make_and_model()  # Output: Club Car Precedent
mygolfcart.moves()  # Output: The vehicle moves
# This code demonstrates inheritance in Python by defining subclasses Airplane, Boat, and golfcart that inherit from the Vehicle class.
# Each subclass overrides the moves method to provide specific behavior for airplanes and boats, while golfcart uses the inherited method from Vehicle.
# Instances of each subclass are created, and their methods are called to show how inheritance and method overriding work in Python. the make and model of the vehicle using an f-string for formatting.
# An instance of the Vehicle class is created, and the get_make_and_model method is called to display the vehicle's details.
# This demonstrates how to define and use methods within a class in Python.

