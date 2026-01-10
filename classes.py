"""
classes.py - Classes, inheritance, and polymorphism.

Learning goals:
- Define classes and instance methods
- Inherit and override methods
- Use super() to call parent behavior
"""


class Vehicle:  # Define a base class for vehicles.
    wheels = 0  # Define a class variable shared by all vehicles.

    def __init__(self, make, model):  # Initialize a vehicle instance.
        self.make = make  # Store the manufacturer.
        self.model = model  # Store the model name.

    def moves(self):  # Define a generic movement method.
        print("The vehicle moves")  # Print a generic movement message.

    def get_make_and_model(self):  # Define a method to format details.
        return f"{self.make} {self.model}"  # Return make and model as a string.

    def __str__(self):  # Define a human-friendly string representation.
        return f"{self.__class__.__name__}({self.get_make_and_model()})"  # Build label.


EXAMPLE_WALKTHROUGH_VEHICLE = """  # Store a walkthrough for Vehicle.
Example Walkthrough: Vehicle
- wheels = 0:
  sets a class variable shared by Vehicle instances.
- def __init__(self, make, model):
  initializes instance attributes make and model.
- def moves(self):
  prints "The vehicle moves".
- def get_make_and_model(self):
  returns a string like "Toyota Corolla".
- def __str__(self):
  returns a label like "Vehicle(Toyota Corolla)".
Example usage:
- car = Vehicle("Toyota", "Corolla")
- str(car) returns "Vehicle(Toyota Corolla)".
"""


class Airplane(Vehicle):  # Define a subclass for airplanes.
    def __init__(self, make, model, wings):  # Initialize airplane with wings.
        super().__init__(make, model)  # Initialize parent fields.
        self.wings = wings  # Store wings description.

    def moves(self):  # Override movement behavior.
        print("The airplane flies")  # Print airplane-specific movement.


EXAMPLE_WALKTHROUGH_AIRPLANE = """  # Store a walkthrough for Airplane.
Example Walkthrough: Airplane
- class Airplane(Vehicle):
  inherits from Vehicle.
- super().__init__(make, model):
  initializes Vehicle fields.
- self.wings = wings:
  stores airplane-specific data.
- def moves(self):
  overrides Vehicle.moves to print "The airplane flies".
Example usage:
- plane = Airplane("Boeing", "747", "Two")
- plane.moves() prints "The airplane flies".
"""


class Boat(Vehicle):  # Define a subclass for boats.
    def moves(self):  # Override movement behavior.
        print("The boat sails")  # Print boat-specific movement.


EXAMPLE_WALKTHROUGH_BOAT = """  # Store a walkthrough for Boat.
Example Walkthrough: Boat
- class Boat(Vehicle):
  inherits from Vehicle.
- def moves(self):
  overrides Vehicle.moves to print "The boat sails".
Example usage:
- boat = Boat("Yamaha", "242X")
- boat.moves() prints "The boat sails".
"""


class GolfCart(Vehicle):  # Define a subclass for golf carts.
    wheels = 4  # Override wheels for golf carts.


EXAMPLE_WALKTHROUGH_GOLFCART = """  # Store a walkthrough for GolfCart.
Example Walkthrough: GolfCart
- class GolfCart(Vehicle):
  inherits from Vehicle.
- wheels = 4:
  overrides the class variable for golf carts.
Example usage:
- cart = GolfCart("Club Car", "Precedent")
- cart.wheels is 4.
"""


def demo_objects():  # Define a demo that creates and uses objects.
    print("\nObjects")  # Print a demo header.
    print("-------")  # Print an underline for the header.
    mycar = Vehicle("Toyota", "Corolla")  # Create a Vehicle instance.
    myplane = Airplane("Boeing", "747", "Two")  # Create an Airplane instance.
    myboat = Boat("Yamaha", "242X")  # Create a Boat instance.
    mycart = GolfCart("Club Car", "Precedent")  # Create a GolfCart instance.

    print("mycar:", mycar.get_make_and_model())  # Show car details.
    print("myplane:", myplane.get_make_and_model())  # Show plane details.
    print("myboat:", myboat.get_make_and_model())  # Show boat details.
    print("mycart:", mycart.get_make_and_model())  # Show cart details.

    for v in (mycar, myplane, myboat, mycart):  # Iterate over vehicles.
        v.moves()  # Call the polymorphic moves method.
        print("str:", str(v), "wheels:", v.wheels)  # Print object string and wheels.


EXAMPLE_WALKTHROUGH_DEMO = """  # Store a walkthrough for demo_objects.
Example Walkthrough: demo_objects
- print("\\nObjects"):
  prints a blank line then "Objects".
- print("-------"):
  prints an underline.
- mycar = Vehicle("Toyota", "Corolla"):
  creates a Vehicle instance.
- myplane = Airplane("Boeing", "747", "Two"):
  creates an Airplane instance.
- myboat = Boat("Yamaha", "242X"):
  creates a Boat instance.
- mycart = GolfCart("Club Car", "Precedent"):
  creates a GolfCart instance.
- print("mycar:", mycar.get_make_and_model()):
  outputs: mycar: Toyota Corolla
- print("myplane:", myplane.get_make_and_model()):
  outputs: myplane: Boeing 747
- print("myboat:", myboat.get_make_and_model()):
  outputs: myboat: Yamaha 242X
- print("mycart:", mycart.get_make_and_model()):
  outputs: mycart: Club Car Precedent
- for v in (...):
  iterates over all vehicles.
- v.moves():
  prints movement for each type.
- print("str:", str(v), "wheels:", v.wheels):
  prints each object's label and wheels count.
"""


NOTES = """  # Store study notes as a multiline string.
Notes:
- self is the instance; methods can read and modify instance data.
- Inheritance lets subclasses reuse and override behavior.
- Polymorphism lets different classes share the same interface.
"""


QUESTIONS = """  # Store practice questions as a multiline string.
Questions:
1) What is the difference between a class variable and an instance variable?
2) Why do we call super().__init__ in Airplane?
3) What happens if a subclass does not override moves?
4) When should you use composition instead of inheritance?
"""


def main():  # Define the script entry point.
    demo_objects()  # Run the object demo.
    print(NOTES.strip())  # Print notes without extra whitespace.
    print()  # Print a blank line between notes and questions.
    print(QUESTIONS.strip())  # Print questions for review.


EXAMPLE_WALKTHROUGH_MAIN = """  # Store a walkthrough for main.
Example Walkthrough: main
- demo_objects():
  runs the object creation and polymorphism demo.
- print(NOTES.strip()):
  prints the Notes block.
- print():
  prints a blank line.
- print(QUESTIONS.strip()):
  prints the Questions block.
"""


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
