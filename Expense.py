

class Expense:
    def __init__(self, name, amount, date):
        self.name = name
        self.amount = amount
        self.date = date

    def show(self):
        print(self.date, '   ', self.name, ': ', self.amount)
