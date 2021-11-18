from database_connection import get_database_connection
from repository.house_repository import HouseRepository
from repository.transaction_repository import TransactionsRepository

class Menu:
    def __init__(self):
        self.commands = [
            {'command':'1','description':'Raportti'},
            {'command':'2','description':'Asunnot'},
            {'command':'3','description':'Luo uusi asunto'},
            {'command':'4','description':'Lisää/muokkaa asunnon tuloja ja menoja'},
            {'command':'5','description':'Muokkaa asunnon tietoja'},
            {'command':'X','description':'Poistu'},
        ]
        self._house_repository = HouseRepository(get_database_connection())
        self._transaction_repository = TransactionsRepository(get_database_connection())
        self.houses = self._house_repository.get_houses()
        
    def print_commands(self):
        print('Saatavilla olevat ominaisuudet:')
        for command in self.commands:
            print(f"{command['command']} {command['description']}")
    
    def setup_houses(self):
        self.houses = self._house_repository.get_houses()

    def command_line_runner(self):
        
        self.print_commands()
        
        while True:
            command = input('komento: ')

            if command == '1':
                self.print_report()
            elif command == '2':
                self.print_houses()
            elif command == '3':
                self.new_house()
            elif command == '4':
                self.add_edit_transactions()
            elif command == '5':
                self.update_house_info()
            elif command == 'help':
                self.print_commands()
            elif command == 'X':
                break
            else:
                print('Väärä syöte')
    
    def print_report(self):
        pass

    def print_houses(self):
        if len(self.houses) == 0:
            print('ei asuntoja')
        else:
            for house in self.houses:
                print(f"{house.id} {house.name}  {house.address}")

    def new_house(self):
        new_house_name = input('Asunnon nimi: ')
        new_house_address = input('Osoite: ')
        self._house_repository.create_house(new_house_name,new_house_address)
        self.setup_houses()

    def update_house_info(self):
        pass

    
    def add_edit_transactions(self):
        
        add_edit_commands = [
            {'command':'1','description':'Uusi tulo'},
            {'command':'2','description':'Uusi meno'},
            {'command':'3','description':'muokkaa tuloa'},
            {'command':'4','description':'muokkaa menoa'},
            {'command':'X','description':'Palaa päävalikkoon'}

        ]
        
        while True:
            command = input('Komento: ')

            if command == '1':
                house_id = input('Talo id: ')
                category_id = input('Kategoria: ')
                amount = input('Summa: ')
                description = input('Selite: ')
                new_transaction = self._transaction_repository.add_income(house_id,category_id,amount,description)
            elif command == '2':
                house_id = input('Talo id: ')
                category_id = input('Kategoria: ')
                amount = input('Summa: ')
                description = input('Selite: ')
                new_transaction = self._transaction_repository.add_expense(house_id,category_id,amount,description)
            elif command == '3':
                pass
            elif command == '4':
                pass
            elif command == 'X':
                break
            else:
                print('Väärä syöte')