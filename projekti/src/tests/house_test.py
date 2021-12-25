import unittest

from database_connection import get_database_connection
from repository.house_repository import HouseRepository
from services.house_services import HouseService

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.cursor = HouseRepository(get_database_connection())
        self.cursor.delete_all()
        self.cursor.create_house('testHouse','testAddress')
        self.house_service = HouseService()

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

    def test_house_service_get_houses(self):
        houses = self.house_service.get_houses()
        self.assertEqual(len(houses),1)

    def test_house_service_add_new_house(self):
        self.house_service.new_house('NewHouse','HouseAddress')
        houses = self.cursor.get_houses()
        self.assertEqual(len(houses),2)

    def test_house_service_edit_house_info(self):
        house_to_update = self.house_service.get_houses()[0]
        self.house_service.update_house_info(house_to_update.id,'UpdatedName','Newaddress')
        updated_house = self.house_service.get_houses()[0]
        self.assertEqual(updated_house.name,'UpdatedName')
        self.assertEqual(updated_house.address,'Newaddress')

    def test_house_service_report_of_all_houses(self):
        report = self.house_service.report_of_all_houses()
        self.assertEqual(report[0]['incomes'],0)
        self.assertEqual(report[0]['expenses'],0)
        self.assertEqual(report[0]['name'],'testHouse')
