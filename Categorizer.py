from enum import Enum


class Categorizer:
    class Category(Enum):
        living = 1
        saving = 2
        fun = 3

    def __init__(self, book):
        self.book = book

    def get_category(self, expense):
        return self.Category.living.name
