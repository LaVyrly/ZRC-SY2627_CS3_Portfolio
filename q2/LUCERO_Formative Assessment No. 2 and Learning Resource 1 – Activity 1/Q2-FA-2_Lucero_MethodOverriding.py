# Parent class: Patient
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = float(bill_amount)

    # Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = float(bill_amount)

    # Base calculate_bill method (Regular patient pays full amount)
    def calculate_bill(self):
        return self.__bill_amount


# Child class: SeniorPatient (20% discount)
class SeniorPatient(Patient):
    def calculate_bill(self):
        # Apply 20% discount
        return self.get_bill_amount() * 0.80


# Child class: PhilHealthPatient (15% discount)
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        # Apply 15% discount
        return self.get_bill_amount() * 0.85


# Instantiating one object per class
regular_patient = Patient("LaVyrly D. Lucero", 67000000)
senior_patient = SeniorPatient("Princess Sofia Roda", 690000000000000)
philhealth_patient = PhilHealthPatient("Noreen Ysabelle C. Angangan", 10100000)

# Storing objects in a list for clean display output
patients = [regular_patient, senior_patient, philhealth_patient]

print("Hospital Billing System")
print("-----------------------")

for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill: P{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: P{patient.calculate_bill():,.2f}\n")