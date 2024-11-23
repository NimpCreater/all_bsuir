class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def total_expenses(self, category):
        
        return self.expenses.get(category, 0)  

    def all_categories(self):
   
        return list(self.expenses.keys())


tracker = ExpenseTracker()


tracker.add_expense("Продукты", 1000)
tracker.add_expense("Бензин", 500)
tracker.add_expense("Продукты", 300)  
tracker.add_expense("Развлечения", 1500)

# Проверяем общую сумму расходов по категориям
print(f"Общие расходы на Продукты: {tracker.total_expenses('Продукты')}")  
print(f"Общие расходы на Бензин: {tracker.total_expenses('Бензин')}") 
print(f"Общие расходы на Развлечения: {tracker.total_expenses('Развлечения')}")  

print("Все категории расходов:", tracker.all_categories())  

print(f"Общие расходы на Одежду: {tracker.total_expenses('Одежда')}") 
