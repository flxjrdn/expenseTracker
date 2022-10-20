from Expense import Expense
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


class Book:
    __horizon: date = date(2022, 12, 31)

    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, date):
        self.expenses.append(Expense(name, amount, date))

    def add_monthly_expense(self, name, amount, start, finish):
        d = start
        while (d <= finish) & (d <= self.__horizon):
            self.expenses.append(Expense(name, amount, d))
            d = d + relativedelta(months=+1)

    def show_expenses(self):
        for expense in self.expenses:
            expense.show()

    def get_expenses(self, year, month):
        return [exp for exp in self.expenses if exp.in_month(year, month)]

    def to_df(self):
        expenses = []
        for exp in self.expenses:
            expenses.append(exp.to_list())
        df = pd.DataFrame(expenses,
                          columns=Expense.get_attributes())
        return df

    def clear_expenses(self):
        self.expenses = []

    def from_df(self, df: pd.DataFrame):
        self.clear_expenses()
        for i in df.index:
            exp = Expense.from_df_row(df.iloc[i])
            self.expenses.append(exp)

    def sorted_expenses(self):
        df = self.to_df()
        df.sort_values(by=['date', 'name', 'amount'],
                       inplace=True)
        return df
