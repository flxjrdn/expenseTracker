from enum import Enum
from Expense import Expense


class Categorizer:
    mapping = dict()

    class Category(Enum):
        living = 1
        saving = 2
        fun = 3
        clothing = 4

    def create_mapping(self):
        self.mapping['etf-1'] = self.Category.saving
        self.mapping['etf-2'] = self.Category.saving

        self.mapping['rent'] = self.Category.living
        self.mapping['groceries'] = self.Category.living
        self.mapping['internet'] = self.Category.living
        self.mapping['phone'] = self.Category.living

        self.mapping['shirt'] = self.Category.clothing
        self.mapping['jeans'] = self.Category.clothing

        self.mapping['restaurant'] = self.Category.fun
        self.mapping['spotify'] = self.Category.fun
        self.mapping['streaming'] = self.Category.fun

    def __init__(self, book):
        self.book = book
        self.create_mapping()

    def get_category(self, expense: Expense):
        return self.mapping[expense.name].name
