# Parent class
class Animal:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    def make_sound(self):
        print(self.get_name(), "makes a sound.")

    def eat(self):
        print(self.get_name(), "is eating.")


# Child class: Lion
class Lion(Animal):
    def make_sound(self):
        print(self.get_name(), "roars loudly!")

    def eat(self):
        print(self.get_name(), "eats fresh meat.")


# Child class: Elephant
class Elephant(Animal):
    def make_sound(self):
        print(self.get_name(), "trumpets!")

    def eat(self):
        print(self.get_name(), "eats grass and fruits.")


# Child class: Monkey
class Monkey(Animal):
    def make_sound(self):
        print(self.get_name(), "chatters!")

    def eat(self):
        print(self.get_name(), "eats bananas.")


# Create objects for each child class
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# Execute methods using a for loop
animals = [lion, elephant, monkey]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print("-----")