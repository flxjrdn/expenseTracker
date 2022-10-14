import Book
import datetime

if __name__ == '__main__':
    print('Expense Tracker v0.1')

    book = Book.Book()
    book.add_expense('groceries', 19.95, datetime.date(2022, 1, 10))
    book.show_expenses()
