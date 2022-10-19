from Book import Book


class Writer:
    book: Book

    def __init__(self, book: Book):
        self.book = book

    def to_csv(self):
        df = self.book.sorted_expenses()
        df.to_csv('expenses.csv', index=False)
