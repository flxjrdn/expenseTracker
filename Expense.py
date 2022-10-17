from datetime import date


class Expense:
    date: date

    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date

    def show(self):
        print(self.date, '   ', self.name, ': ', self.amount)

    def in_month(self, year, month):
        return (year == self.date.year) & (month == self.date.month)

    def to_list(self):
        return [self.name, self.amount, self.date]
