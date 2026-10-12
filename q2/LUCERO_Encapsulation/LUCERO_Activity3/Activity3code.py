class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = 0
        
        self.account_number = account_number
        self.balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = float(value)
        else:
            print("The balance must be not be a negative number.")


if __name__ == "__main__":
  
    a1 = BankAccount(91212, 2900.00)

    print("Account 1")
    print("Account Number:", a1.account_number)
    print(f"Balance: {a1.balance:.2f}")

    print("\nUpdate balance to -200")
    a1.balance = -200

    print("Account Number:", a1.account_number)
    print(f"Balance: {a1.balance:.2f}")