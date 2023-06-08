import sqlite3 as sql3


class Database:
    """
    Instantiate the Class and create a table with the name passed in the
    argument.

    Ex.:
    db = DataBase("dbname")

    >>> <__main__.DataBase object>
    """

    def __init__(self, name: str):
        self._dbconnection = self._createdb(name)
        self._dbcursor = self._dbconnection.cursor()
        self.tables: list = []

    def _createdb(self, databasename: str) -> sql3.Connection:
        con = sql3.connect(databasename + '.db')
        return con

    def create_simple_table(self, name: str, columns: str):
        """
        Create a table in a database.

        Args:
            name (str): Table name
            columns (str): Column names

        Ex.:
        db.createsimpletable(name='Tablename', columns='Col1, Col2, Col3' )
        """

        if isinstance(name, str) and isinstance(columns, str):

            table = f' Table Name: "{name}" | Columns: "{columns}" '
            self.tables.append(table)

            sqlstatement = f"CREATE TABLE {name}({columns})"
            self._dbcursor.execute(sqlstatement)

            print(
                f"Table created successfully | Name:{name}, Columns:{columns}")

        else:
            print("The table 'name' and 'columns' must be of type 'str'")

    def insert_data_in_simple_table(self, tablename: str, values: list):
        """
        insert data into a simple table where:
        >data of type str = TEXT;
        >data of type int = INTERGER;
        >data of type float = REAL;
        >data of type None = NULL;

        Args:
            tablename (str): Table name
            value (list): list of values according to the number of columns

        Ex.:
        db.nsert_data_in_simple_table(
            tablename="table", values='text', 1, 1.1, '')
        """

        placeholders = ','.join(['?' for _ in values])
        sqlstatement = f"INSERT INTO {tablename} VALUES ({placeholders})"
        self._dbcursor.execute(sqlstatement, values)
        self._dbconnection.commit()

    def delete_data_in_simple_table(self, tablename: str, condition: str):
        """
        Deletes data from a simple database table based on a condition.

        Args:
            tablename (str): Table name.
            condition (str): Condition to filter the rows to be deleted.

        Ex.:
        db.delete_data_in_simple_table(
            tablename="table", condition="column1 = 'value'")
        """

        sqlstatement = f"DELETE FROM {tablename} WHERE {condition}"
        self._dbcursor.execute(sqlstatement)
        self._dbconnection.commit()

    def replace_data_in_simple_table(self, tablename: str, values: list):
        """
        Replaces data into a simple database table.

        Args:
            tablename (str): Table name.
            values (list): List of values to replace.

        Ex.:
        db.replace_data_in_simple_table(
            tablename="table", values=['text', 1, 1.1, None]
        """

        placeholders = ','.join(['?' for _ in values])
        sqlstatement = f"REPLACE INTO {tablename} VALUES ({placeholders})"
        self._dbcursor.execute(sqlstatement, values)
        self._dbconnection.commit()

    def query_data(self, tablename: str, values: list):
        pass


if __name__ == "__main__":
    pass
