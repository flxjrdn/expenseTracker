import Expense


class Book:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, date):
        expense = Expense.Expense(name, amount, date)
        self.expenses.append(expense)

    def show_expenses(self):
        for expense in self.expenses:
            expense.show()
