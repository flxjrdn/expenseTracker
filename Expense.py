from datetime import datetime
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

    @staticmethod
    def from_df_row(df_row):
        d = datetime.strptime(df_row['date'], '%Y-%m-%d').date()
        expense = Expense(df_row['name'],
                          df_row['amount'],
                          d)
        return expense

    @staticmethod
    def get_attributes():
        return ['name',
                'amount',
                'date']
