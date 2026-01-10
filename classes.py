"""
classes.py - Classes, inheritance, and polymorphism.

Learning goals:
- Define classes and instance methods
- Inherit and override methods
- Use super() to call parent behavior
"""


class Vehicle:
    wheels = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("The vehicle moves")

    def get_make_and_model(self):
        return f"{self.make} {self.model}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.get_make_and_model()})"


class Airplane(Vehicle):
    def __init__(self, make, model, wings):
        super().__init__(make, model)
        self.wings = wings

    def moves(self):
        print("The airplane flies")


class Boat(Vehicle):
    def moves(self):
        print("The boat sails")


class GolfCart(Vehicle):
    wheels = 4


def demo_objects():
    print("\nObjects")
    print("-------")
    mycar = Vehicle("Toyota", "Corolla")
    myplane = Airplane("Boeing", "747", "Two")
    myboat = Boat("Yamaha", "242X")
    mycart = GolfCart("Club Car", "Precedent")

    print("mycar:", mycar.get_make_and_model())
    print("myplane:", myplane.get_make_and_model())
    print("myboat:", myboat.get_make_and_model())
    print("mycart:", mycart.get_make_and_model())

    for v in (mycar, myplane, myboat, mycart):
        v.moves()
        print("str:", str(v), "wheels:", v.wheels)


NOTES = """
Notes:
- self is the instance; methods can read and modify instance data.
- Inheritance lets subclasses reuse and override behavior.
- Polymorphism lets different classes share the same interface.
"""


QUESTIONS = """
Questions:
1) What is the difference between a class variable and an instance variable?
2) Why do we call super().__init__ in Airplane?
3) What happens if a subclass does not override moves?
4) When should you use composition instead of inheritance?
"""


def main():
    demo_objects()
    print(NOTES.strip())
    print()
    print(QUESTIONS.strip())


if __name__ == "__main__":
    main()
