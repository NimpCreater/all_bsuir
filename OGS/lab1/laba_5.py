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


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        super().__init__(owner, balance, "Сберегательный счет")

    def withdraw(self, amount):
        print("Снятие со сберегательного счета невозможно.")
    
   
        
      


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance):
        self.owner = owner        
        self.balance = balance
        super().__init__(owner, balance, "Текущий счет")

    def deposit(self, amount):
        if amount <= 0:
            return ("Некорректная сумма для пополнения.")
        if amount > 5000:
            bonus = amount * 0.01
        else:
            bonus = 0
        self.balance += amount + bonus
        print(f"Пополнение счета на {amount} рублей выполнено. Текущий баланс: {self.balance}.")





account1 = BankAccount("Oksana Shevchuk", 1000, 'Rich')
account2_savings = SavingsAccount("Pavel Dedkov", 0)
account3_checking = CheckingAccount("Ivan Ivanov", 790)

account1.deposit(500)
account1.withdraw(200)

account2_savings.deposit(5000)
account2_savings.withdraw(200)

account3_checking.deposit(5000)
account3_checking.withdraw(200)

account1.display_account_info()
account2_savings.display_account_info()
account3_checking.display_account_info()