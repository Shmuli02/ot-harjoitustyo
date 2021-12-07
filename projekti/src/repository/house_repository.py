from house import House

def get_house_by_row(row):
    return House(row['house_id'],row['name'],row['address']) if row else None

class HouseRepository:
    def __init__(self, connection):
        self._connection = connection

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute('delete from house')
        self._connection.commit()

    def create_house(self,name,address):

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO house (name,address) values (?, ?)',
            (name,address)
        )

        self._connection.commit()

    def get_houses(self):

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM house')

        rows = cursor.fetchall()

        return list(map(get_house_by_row, rows))

    def edit_house_info(self,house_id,name,address):
        cursor = self._connection.cursor()
        cursor.execute(
            'UPDATE house SET name=?,address=? WHERE house_id=?',
            (name,address,house_id)
        )
        self._connection.commit()

    def get_house_by_id(self,house_id):
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM house WHERE house_id=?',
            (house_id)
        )
        rows = cursor.fetchall()
        return list(map(get_house_by_row, rows))
