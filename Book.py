import Expense
import numpy as np
from datetime import date
from dateutil.relativedelta import relativedelta


class Book:
    __horizon: date = date(2022, 12, 31)

    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, date):
        self.expenses.append(Expense.Expense(name, amount, date))

    def add_monthly_expense(self, name, amount, start, finish):
        d = start
        while (d <= finish) & (d <= self.__horizon):
            self.expenses.append(Expense.Expense(name, amount, d))
            d = d + relativedelta(months=+1)

    def show_expenses(self):
        for expense in self.expenses:
            expense.show()

    def get_expenses(self, year, month):
        return [exp for exp in self.expenses if exp.in_month(year, month)]

    def sort(self):
        e = np.array([exp.to_list() for exp in self.expenses])
        return e
