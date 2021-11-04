from house import House

def get_house_by_row(row):
    return House(row['name'],row['address']) if row else None

class HouseRepository:
    def __init__(self, connection):
        self._connection = connection

    def createHouse(self,name,address):

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO house (name,address) values (?, ?)',
            (name,address)
        )

        self._connection.commit()
    
    def getHouses(self):

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM house')

        rows = cursor.fetchall()

        return list(map(get_house_by_row, rows))