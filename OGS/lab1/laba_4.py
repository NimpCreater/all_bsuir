

#var = 4? 

class BankAccount:
    def __init__(self, owner, balance, account_type):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount <= 0:
            return ("Некорректная сумма для пополнения.")
        self.balance += amount
        print(f"Пополнение счета на {amount} рублей выполнено. Текущий баланс: {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            return ("Некорректная сумма для снятия или недостаточно средств на счете.") 
        self.balance -= amount
        print(f"Снятие счета на {amount} рублей выполнено. Текущий баланс: {self.balance}.")

    def display_account_info(self):
        print(f"Владелец: {self.owner}")
        print(f"Тип счета: {self.account_type}")
        print(f"Баланс: {self.balance}")
    

account1 = BankAccount("Oksana Shevchuk", 1000, "Rich")
account2 = BankAccount("Pavel Dedkov", 0, "Poor")

account1.deposit(500)
account2.withdraw(200)


account1.display_account_info()
account2.display_account_info()