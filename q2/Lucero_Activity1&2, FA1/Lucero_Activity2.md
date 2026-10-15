1. For each code example on single, multilevel, and hierarchical inheritance, create the
corresponding class diagram in your notebook. Clearly identify the attributes and methods of
each class. Show the correct inheritance relationship between classes.

  * Single Inheritance

    <img width="355" height="613" alt="Screenshot 2026-10-15 140146" src="https://github.com/user-attachments/assets/1e8d60f4-2f61-4655-bd31-a40ff8361340" />


  * Multilevel Inheritance

    <img width="296" height="707" alt="Screenshot 2026-10-15 141638" src="https://github.com/user-attachments/assets/9eda1c66-97a2-4b98-9c16-4604ace07eba" />


  * Hierarchical Inheritance

    <img width="1038" height="679" alt="Screenshot 2026-10-15 142201" src="https://github.com/user-attachments/assets/e614e0d2-1027-4807-a41e-eac200a9078d" />


2. Run the code examples in your IDE. Modify the code by adding getter and setter methods,
changing object values, adding new objects, and adjusting method outputs. Observe how
these changes affect the program. Experiment freely to strengthen your understanding of
inheritance.

  * Example 1: Animal, Dog, and Cat Code Modifications

class Animal:
    def __init__(self, name):
        self.__name = name  
    # Getter and Setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def eat(self):
        print(f"[Feeding Time] {self.__name} is currently eating.")

    def sleep(self):
        print(f"[Rest Time] {self.__name} is fast asleep.")



class Dog(Animal):
    def bark(self):
        print(f"{self.get_name()} barks: Woof! Woof!")


class Cat(Animal):
    def meow(self):
        print(f"{self.get_name()} meows: Purr... Meow!")



animal1 = Animal("Generic Animal")
dog1 = Dog("Bruno")
cat1 = Cat("Kitty")
dog2 = Dog("Max")  # Added new object


print("--- Initial Animal Behaviors ---")
animal1.eat()
animal1.sleep()

dog1.eat()
dog1.bark()

cat1.sleep()
cat1.meow()


print("\n--- After Modifying Values and Adding New Object ---")
dog2.set_name("Rocky")
dog2.eat()
dog2.bark()

  * Example 2: Person, Employee, and Manager Code Modifications

    
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age



class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.__job_title = job_title
        self.__salary = salary

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary



class Manager(Employee):
    def __init__(self, name, age, job_title, salary, department):
        super().__init__(name, age, job_title, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department


    def display_info(self):
        print(f"Name: {self.get_name()}")
        print(f"Age: {self.get_age()}")
        print(f"Job Title: {self.get_job_title()}")
        print(f"Salary: ${self.get_salary():,}")
        print(f"Department: {self.get_department()}\n")



manager1 = Manager("Alice", 35, "Project Manager", 80000, "IT")[cite: 8, 26]
manager2 = Manager("David", 42, "Operations Manager", 95000, "Logistics")  # Added new object

print("--- Initial Manager Profiles ---")
manager1.display_info()
manager2.display_info()


print("--- After Modifying Manager 1 Values ---")
manager1.set_name("Alicia")
manager1.set_salary(85000)
manager1.set_department("Software Engineering")
manager1.display_info()
