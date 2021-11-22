class Menu:
    def __init__(self,ui,house_repository,transaction_repository):
        self.ui = ui
        self.main_commands = [
            {'command':'1','description':'Raportti'},
            {'command':'2','description':'Asunnot'},
            {'command':'3','description':'Luo uusi asunto'},
            {'command':'4','description':'Lisää/muokkaa asunnon tuloja ja menoja'},
            {'command':'5','description':'Muokkaa asunnon tietoja'},
            {'command':'X','description':'Poistu'},
        ]
        self.transaction_commands = [
            {'command':'1','description':'Uusi tulo'},
            {'command':'2','description':'Uusi meno'},
            {'command':'3','description':'muokkaa tuloa'},
            {'command':'4','description':'muokkaa menoa'},
            {'command':'X','description':'Palaa päävalikkoon'}

        ]
        self._house_repository = house_repository
        self._transaction_repository = transaction_repository
        self.setup_houses()
    
    def setup_houses(self):
        self.houses = self._house_repository.get_houses()
        self.transactions = self._transaction_repository.get_transactions()
        ## transaction to houses
        house_dict = {}
        for house in self.houses:
            house_dict[house.id] = house
        for transaction in self.transactions:
            if transaction.transaction_type == 'income':
                house_dict[transaction.house_id].incomes.append(transaction)
            else:
                house_dict[transaction.house_id].expenses.append(transaction)

    def print_main_commands(self):
        self.ui.print('Saatavilla olevat ominaisuudet:')
        for command in self.main_commands:
            self.ui.print(f"{command['command']} {command['description']}")

    def print_transaction_commands(self):
        self.ui.print('Tapahtumien komennot:')
        for command in self.transaction_commands:
            self.ui.print(f"{command['command']} {command['description']}")
    
    def get_house_by_id(self,id):
        try:
            return [x for x in self.houses if x.id == int(id)][0] if not [] else None
        except:
            return None
        

    
    def command_line_runner(self):
        
        self.print_main_commands()
        
        while True:
            command = self.ui.read('komento: ')

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
                self.print_main_commands()
            elif command == 'X':
                break
            else:
                self.ui.print('Väärä syöte. Apua saat komennolla (help)')
    
    def print_report(self):
        self.ui.print(f"{'Asunto':20}{'Tulot':20} Menot")
        incomes = 0
        expenses = 0
        for house in self.houses:
            report = house.house_report()
            incomes += report['incomes']
            expenses += report['expenses']
            self.ui.print(f"{house.name} {report['incomes']:20} {report['expenses']:20}")
        self.ui.print(f"Yht. {incomes:20} {expenses:20}")

    def print_houses(self):
        if len(self.houses) == 0:
            self.ui.print('ei asuntoja')
        else:
            for house in self.houses:
                self.ui.print(f"{house.id} {house.name}  {house.address}")

    def new_house(self):
        new_house_name = self.ui.read('Asunnon nimi: ')
        new_house_address = self.ui.read('Osoite: ')
        self._house_repository.create_house(new_house_name,new_house_address)
        self.setup_houses()

    def update_house_info(self):
        house_id=self.ui.read('Talo id: ')
        house = self.get_house_by_id(house_id)
        print(house)
        if house:
            new_name = self.ui.read(f"Asunnon nimi ({house.name})") if not '' else house.name #ei toimi
            new_address = self.ui.read(f"Asunnon osoite ({house.address})") if not '' else house.address #ei toimi
        else:
            self.ui.print('Asuntoa ei löytynyt')

    
    def add_edit_transactions(self):
        
        
        self.print_transaction_commands()
        while True:
            command = self.ui.read('Komento: ')

            if command == '1':
                house_id = self.ui.read('Talo id: ')
                house = self.get_house_by_id(house_id)
                if house:
                    category_id = self.ui.read('Kategoria: ')
                    amount = self.ui.read('Summa: ')
                    description = self.ui.read('Selite: ')
                    new_transaction = self._transaction_repository.add_income(house_id,category_id,amount,description)
                else:
                    self.ui.print('Asuntoa ei löytynyt')
            elif command == '2':
                house_id = self.ui.read('Talo id: ')
                house = self.get_house_by_id(house_id)
                if house:
                    category_id = self.ui.read('Kategoria: ')
                    amount = self.ui.read('Summa: ')
                    description = self.ui.read('Selite: ')
                    new_transaction = self._transaction_repository.add_expense(house_id,category_id,amount,description)
                else:
                    self.ui.print('Asuntoa ei löytynyt')
            elif command == '3':
                pass
            elif command == '4':
                pass
            elif command == 'help':
                self.print_transaction_commands()
            elif command == 'X':
                break
            else:
                self.ui.print('Väärä syöte. Apua saat komennolla (help)')
