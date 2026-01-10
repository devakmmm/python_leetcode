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


class Airplane(Vehicle):  # Define a subclass for airplanes.
    def __init__(self, make, model, wings):  # Initialize airplane with wings.
        super().__init__(make, model)  # Initialize parent fields.
        self.wings = wings  # Store wings description.

    def moves(self):  # Override movement behavior.
        print("The airplane flies")  # Print airplane-specific movement.


class Boat(Vehicle):  # Define a subclass for boats.
    def moves(self):  # Override movement behavior.
        print("The boat sails")  # Print boat-specific movement.


class GolfCart(Vehicle):  # Define a subclass for golf carts.
    wheels = 4  # Override wheels for golf carts.


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


if __name__ == "__main__":  # Run main only when executed directly.
    main()  # Invoke the entry point.
