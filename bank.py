class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"name = {self.name}, age = {self.age}"


class Bank(User):
    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{self.name}'s account balance is ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"{self.name}'s account balance is ${self.balance}"
        else:
            print(f'Insufficent funds, Account Balance: ${self.balance}')
        

if __name__ == "__main__":
    mo = Bank('Mohammed Qureshi', 21, 1382)
    adnan = Bank('Adnan Khan', 35, 545)
    print(mo.deposit(12))
    print(adnan.withdraw(75))
    print(adnan.withdraw(1000))



