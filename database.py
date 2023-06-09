import sqlite3 as sql3


class Database:
    """
    Instanciar para criar um banco de dados e uma conexão.

    Ex.:
    db = DataBase("dbname")

    >>> <Database object>
    """

    def __init__(
            self,
            name: str
    ):
        self._dbconnection = self._createdb(name)
        self._dbcursor = self._dbconnection.cursor()
        self.tables: list = []

    def _createdb(
            self,
            databasename: str
    ) -> sql3.Connection:

        con = sql3.connect(databasename + '.db')
        print('Database created successfully:', con)
        return con

    def create_simple_table(
            self,
            name: str,
            columns: str
    ):
        """
        Crie uma tablena no banco de dados.

        CREATE TABLE "nome_tabela"(
            "coluna 1" "tipo_dados_para_coluna_1",
            "coluna 2" "tipo_dados_para_coluna_2",
        );

        Args:
            name (str): Nome da tabela
            columns (str): Nome da Coluna e Tipo de Dado

        Ex.:
        db.create_simple_table(
            name='Nome', columns='Col1 char(50), Col2 (integer), Col3' (real)
            )
        """

        if isinstance(name, str) and isinstance(columns, str):

            table = f'Nome da Tabela: "{name}" | Colunas: "{columns}"'
            self.tables.append(table)

            sqlstatement = f"CREATE TABLE {name} ({columns})"
            self._dbcursor.execute(sqlstatement)

            print(
                f"Table created successfully | Name:{name}, Columns:{columns}")

        else:
            print("The table 'name' and 'columns' must be of type 'str'")

    def insert_data_in_simple_table(
            self,
            table: str,
            values: list
    ):
        """
        Insira dados em uma tabela:
        >data of type str = TEXT;
        >data of type int = INTERGER;
        >data of type float = REAL;
        >data of type None = NULL;

        INSERT INTO "nome_tabela" ("coluna 1", "coluna 2", ...)
        VALUES ("valor 1", "valor 2", ...);

        Args:
            table (str): Nome da Tabela
            value (list): Valores que serão inseridos

        Ex.:
        db.insert_data_in_simple_table(
            table="Tabela", values="1, 2")
        """

        placeholders = ','.join(['?' for _ in values])
        sqlstatement = f"INSERT INTO {table} VALUES ({placeholders})"
        self._dbcursor.execute(sqlstatement, values)
        self._dbconnection.commit()
        print('Data entered successfully')

    def delete_data_in_simple_table(
            self,
            table: str,
            condition: str
    ):
        """
        Delete dados de uma tabela do banco de dados baseado em uma condição.

        DELETE FROM "nome_tabela"
        WHERE "condição";

        Args:
            table (str): Table name.
            condition (str): Condition to filter the data to be deleted.

        Ex.:
        db.delete_data_in_simple_table(
            table="table", condition="column1 = 'value'")
        """

        sqlstatement = (
            f"DELETE FROM {table} WHERE {condition}"
        )
        self._dbcursor.execute(sqlstatement)
        self._dbconnection.commit()
        print('The data was deleted successfully')

    def update_data_in_simple_table(
            self,
            table: str,
            set: str,
            condition: str
    ):
        """
        Atualize dados em uma tabela do banco de dados.

        UPDATE "nome_tabela"
        SET "coluna 1" = [novo valor]
        WHERE "condição";

        Args:
            table (str): Nome da tabela.
            set (str): Coluna e Novo valor.
            condition (str): Condição onde o novo valor será inserido.

        Ex.:
        db.update_data_in_simple_table(
            table="Tabela",
            set="Col1 = 0",
            condition="Col1 = NULL"
        """

        sqlstatement = (
            f"UPDATE {table} SET {set} WHERE {condition} ")
        self._dbcursor.execute(sqlstatement)
        self._dbconnection.commit()
        print('Update done successfully')

    def select_data_in_simple_table(
            self,
            column: str,
            table: str
    ) -> list:
        """
        Consulte dados em uma tabela do banco de dados.

        SELECT "nome_coluna" FROM "nome_tabela";

        Args:
            column (str): Nome da Coluna
            table (str): Nome da Tabela

        Ex.:
        db.select_data_in_simple_table(
            column="Col1", table="Tabela"
        )

        >>> list
        """

        sqlstatement = f"SELECT {column} FROM {table}"
        data = self._dbcursor.execute(sqlstatement)
        data_list = data.fetchall()
        return data_list


if __name__ == "__main__":

    # Criação e conexão do banco de dados:
    db_system = Database("LOGIN")

    # Criação de tabela:
    db_system.create_simple_table(
        name="usuarios",
        columns="nome, senha"
    )

    # Inserindo dados na tabela:
    db_system.insert_data_in_simple_table(
        table="usuarios",
        values=['Everton', 1234]
    )

    db_system.insert_data_in_simple_table(
        table="usuarios",
        values=['Milena', 4321]
    )

    # Consultando tabelas:
    users = db_system.select_data_in_simple_table(
        column="nome",
        table="usuarios"
    )
    print(users)

    password = db_system.select_data_in_simple_table(
        column='senha',
        table='usuarios'
    )
    print(password)

    # Atualizando dados:
    db_system.update_data_in_simple_table(
        table='usuarios',
        set='senha = 8766',
        condition='senha = 1234'
    )

    # Deletando dados:
    db_system.delete_data_in_simple_table(
        table="usuarios",
        condition="nome = 'Milena'"
    )
