import unittest

from database_connection import get_database_connection
from repository.transaction_repository import TransactionsRepository


class TestIncomeExpence(unittest.TestCase):
    def setUp(self):
        self.cursor = TransactionsRepository(get_database_connection())
        self.cursor.delete_all()

    def test_add_income(self):
        self.cursor.add_income(1,1,670,'Vuokra tulo')
        incomes = self.cursor.get_incomes()
        self.assertEqual(len(incomes),1)

    def test_add_expense(self):
        self.cursor.add_expense(1,1,164.43,'Vastike')
        expenses = self.cursor.get_expenses()
        self.assertEqual(len(expenses),1)
