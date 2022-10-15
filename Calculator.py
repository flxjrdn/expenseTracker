import Book
import numpy as np


class Calculator:

    def __init__(self, book):
        self.book = book

    def sum_month(self, year, month):
        return sum([exp.amount for exp in self.book.get_expenses(year, month)])

    def avg_month(self, year):
        total = 0
        num_months = 0
        for month in np.arange(1, 12):
            exp_month = self.sum_month(year, month)
            total += exp_month
            if exp_month > 0:
                num_months += 1
        return round(total / num_months, 2)
