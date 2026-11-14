from abc import ABC, abstractmethod


# Abstract Base Class
class Sensor(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_reading(self):
        pass


# Child Class: pH Sensor
class PHSensor(Sensor):

    def __init__(self):
        super().__init__("pH Sensor")

    def get_reading(self):
        print(f"[{self.name}] Reading: 7.2 pH (Neutral)")


# Child Class: Temperature Sensor
class TempSensor(Sensor):

    def __init__(self):
        super().__init__("Temperature Sensor")

    def get_reading(self):
        print(f"[{self.name}] Reading: 24.5°C")


print("--- Lab Inventory System ---")

ph_sensor = PHSensor()
ph_sensor.get_reading()

temp_sensor = TempSensor()
temp_sensor.get_reading()

print("----------------------------")


# Task 5: Testing the Abstract Class
my_sensor = Sensor("Generic Sensor")