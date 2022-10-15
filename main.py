import Book
import Calculator
from datetime import date


def create_example_book():
    book = Book.Book()
    book.add_expense('groceries', 19.95, date(2022, 1, 10))
    book.add_expense('groceries', 33.22, date(2022, 1, 14))
    book.add_expense('groceries', 10.15, date(2022, 1, 16))
    book.add_expense('groceries', 54.30, date(2022, 1, 22))
    book.add_expense('etf-1', 700, date(2022, 1, 1))
    book.add_expense('etf-2', 300, date(2022, 1, 1))
    book.add_expense('rent', 800, date(2022, 1, 30))
    book.add_expense('spotify', 9.99, date(2022, 1, 1))
    book.add_expense('restaurant', 40.00, date(2022, 1, 20))
    book.add_expense('jeans', 79.90, date(2022, 1, 10))

    book.add_expense('groceries', 9.34, date(2022, 2, 1))
    book.add_expense('groceries', 58.01, date(2022, 2, 8))
    book.add_expense('groceries', 12.13, date(2022, 2, 19))
    book.add_expense('groceries', 33.30, date(2022, 2, 28))
    book.add_expense('etf-1', 700, date(2022, 2, 1))
    book.add_expense('etf-2', 300, date(2022, 2, 1))
    book.add_expense('rent', 800, date(2022, 2, 28))
    book.add_expense('spotify', 9.99, date(2022, 2, 1))
    book.add_expense('restaurant', 35.00, date(2022, 2, 20))
    book.add_expense('shirt', 59.90, date(2022, 2, 10))
    return book


if __name__ == '__main__':
    print('Expense Tracker v0.1')

    book = create_example_book()
    book.show_expenses()

    calc = Calculator.Calculator(book)
    print(calc.sum_month(2022, 1))
    print(calc.sum_month(2022, 2))
    print(calc.avg_month(2022))
