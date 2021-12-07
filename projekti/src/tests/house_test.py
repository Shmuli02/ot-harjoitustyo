import unittest

from database_connection import get_database_connection
from repository.house_repository import HouseRepository

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.cursor = HouseRepository(get_database_connection())
        self.cursor.delete_all()
        self.cursor.create_house('testHouse','testAddress')

    def test_get_houses(self):
        houses = self.cursor.get_houses()
        self.assertEqual(len(houses),1)

    def test_add_house(self):
        self.cursor.create_house('testHouse2','testAddress2')
        houses = self.cursor.get_houses()
        self.assertEqual(len(houses),2)

    def test_edit_house_info(self):
        self.cursor.edit_house_info(1,'NewHouseName','NewHouseAddress')
        house = self.cursor.get_house_by_id('1')[0]
        self.assertEqual(house.name,'NewHouseName')
        self.assertEqual(house.address,'NewHouseAddress')