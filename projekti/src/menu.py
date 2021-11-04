from house import House

class Menu:
    def __init__(self,houses=[]):
        self.commands = [
            {'command':'1','description':'Raportti'},
            {'command':'2','description':'Asunnot'},
            {'command':'3','description':'Luo uusi asunto'},
            {'command':'4','description':'Lisää/muokkaa asunnon tuloja ja menoja'},
            {'command':'X','description':'Poistu'},
        ]
        self.houses = houses
        
    def printCommands(self):
        print('Saatavilla olevat ominaisuudet:')
        for command in self.commands:
            print(f"{command['command']}  {command['description']}")

    def commandLineRunner(self):
        
        self.printCommands()
        
        while True:
            command = input('komento: ')

            if command == '1':
                self.printReport()
            elif command == '2':
                self.printHouses()
            elif command == '3':
                self.newHouse()
            elif command == '4':
                self.addEditIncomesExpenses()
            elif command == 'X':
                break
            else:
                print('Väärä syöte')
    
    def printReport(self):
        pass

    def printHouses(self):
        if len(self.houses) == 0:
            print('ei asuntoja')
        else:
            for house in self.houses:
                print(f"{house.name}  {house.address}")

    def newHouse(self):
        newHouseName = input('Asunnon nimi: ')
        newHouseAddress = input('Osoite: ')
        newHouse = House(newHouseName,newHouseAddress)
        self.houses.append(newHouse)
    
    def addEditIncomesExpenses(self):
        pass
    
