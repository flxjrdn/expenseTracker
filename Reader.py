from Book import Book
import pandas as pd


class Reader:

    @staticmethod
    def from_csv(path):
        df = pd.read_csv(path)
        book = Book()
        book.from_df(df)
        return book
