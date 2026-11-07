# Parent class: Patient
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = float(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = float(bill_amount)

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        print("Patient Type: Regular Patient")


# Child class: SeniorPatient (20% discount)
class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


# Child class: PhilHealthPatient (15% discount)
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


patients = [
    Patient("Yoanna Glorien C. Cabatingan", 67777766666667000),
    SeniorPatient("Leoanna Amabele B. Lumakin", 1000000000000000000), 
    PhilHealthPatient("Maria Avera Adreya A. Carampil", 799999999777777776000)
]

print("Hospital Billing System")
print("-" * 23)

for p in patients:
    print(f"Patient Name: {p.get_name()}")
    p.display_patient_type()
    print(f"Original Bill: P{p.get_bill_amount():,.2f}")
    print(f"Final Bill: P{p.calculate_bill():,.2f}\n")
