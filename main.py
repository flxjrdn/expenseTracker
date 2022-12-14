from Book import Book
from Calculator import Calculator
from Writer import Writer
from Reader import Reader
from Categorizer import Categorizer
from datetime import date


def create_example_book():
    book = Book()
    book.add_monthly_expense('etf-1', 700,
                             start=date(2022, 1, 1), finish=date(2022, 12, 1))
    book.add_monthly_expense('etf-2', 300,
                             start=date(2022, 1, 1), finish=date(2022, 12, 1))
    book.add_monthly_expense('rent', 800,
                             start=date(2022, 1, 1), finish=date(2022, 12, 1))
    book.add_monthly_expense('spotify', 9.99,
                             start=date(2022, 1, 1), finish=date(2022, 12, 1))
    book.add_monthly_expense('internet', 29.90,
                             start=date(2022, 1, 1), finish=date(2022, 12, 1))

    book.add_expense('groceries', 19.95, date(2022, 1, 10))
    book.add_expense('groceries', 33.22, date(2022, 1, 14))
    book.add_expense('groceries', 10.15, date(2022, 1, 16))
    book.add_expense('groceries', 54.30, date(2022, 1, 22))
    book.add_expense('restaurant', 40.00, date(2022, 1, 20))
    book.add_expense('jeans', 79.90, date(2022, 1, 10))

    book.add_expense('groceries', 9.34, date(2022, 2, 1))
    book.add_expense('groceries', 58.01, date(2022, 2, 8))
    book.add_expense('groceries', 12.13, date(2022, 2, 19))
    book.add_expense('groceries', 33.30, date(2022, 2, 28))
    book.add_expense('restaurant', 35.00, date(2022, 2, 20))
    book.add_expense('shirt', 59.90, date(2022, 2, 10))
    return book


if __name__ == '__main__':
    print('Expense Tracker v0.1')

    # book = create_example_book()

    reader = Reader()
    book = reader.from_csv('expenses.csv')

    book.show_expenses()

    categorizer = Categorizer(book)
    cat = categorizer.get_category(book.get_expenses(2022, 1)[0])
    print(cat)


    calc = Calculator(book)
    print(calc.sum_month(2022, 1))
    print(calc.sum_month(2022, 2))
    print(calc.avg_month(2022))

    writer = Writer(book)
    # writer.to_csv()

