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

    def test_get_transactions(self):
        self.cursor.add_income(1,1,650,'Vuokra tulo')
        transactions = self.cursor.get_transactions()
        self.assertEqual(transactions[0].description,'Vuokra tulo')
        self.assertEqual(len(transactions),1)

    def test_edit_income(self):
        self.cursor.add_income(1,1,650,'Vuokra tulo')
        self.cursor.edit_income(1,1,1,325,'Puolikas vuokra')
        incomes = self.cursor.get_incomes()

        self.assertEqual(len(incomes),1)
        self.assertEqual(incomes[0].amount,325)
        self.assertEqual(incomes[0].description,'Puolikas vuokra')

    def test_edit_expense(self):
        self.cursor.add_expense(1,1,124.99,'Vastike')
        self.cursor.edit_expense(1,1,1,204.76,'Vastike + vesi')
        expenses = self.cursor.get_expenses()

        self.assertEqual(len(expenses),1)
        self.assertEqual(expenses[0].amount,204.76)
        self.assertEqual(expenses[0].description,'Vastike + vesi')
