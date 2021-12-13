from house import House

def get_house_by_row(row):
    return House(row['house_id'],row['name'],row['address']) if row else None

class HouseRepository:
    """House Repository handle house db
    """
    def __init__(self, connection):
        """init house repository

        Args:
            connection: db connection
        """
        self._connection = connection

    def delete_all(self):
        """Delete all houses from db
        """
        cursor = self._connection.cursor()
        cursor.execute('delete from house')
        self._connection.commit()

    def create_house(self,name,address):
        """create new house

        Args:
            name (str): name of the house
            address (str): address of the house
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO house (name,address) values (?, ?)',
            (name,address)
        )

        self._connection.commit()

    def get_houses(self):
        """get all houses

        Returns:
            list: return list of houses
        """

        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM house')

        rows = cursor.fetchall()

        return list(map(get_house_by_row, rows))

    def edit_house_info(self,house_id,name,address):
        """Edit house information

        Args:
            house_id (int): id of the updating house
            name (str): name of the house
            address (str): address of the house
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'UPDATE house SET name=?,address=? WHERE house_id=?',
            (name,address,house_id)
        )
        self._connection.commit()

    def get_house_by_id(self,house_id):
        """Get house by id

        Args:
            house_id (int): id of the house

        Returns:
            list: return list of house
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'SELECT * FROM house WHERE house_id=?',
            (house_id)
        )
        rows = cursor.fetchall()
        return list(map(get_house_by_row, rows))
