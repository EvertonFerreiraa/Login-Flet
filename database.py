import sqlite3


class Database:
    def __init__(self, dbname: str):
        """
        Gerar uma Conexão com um banco de Dados SQLite.

        Ex.:
        db = Database("exemplo")

        """
        self._dbconnection = self._connectdb(dbname)
        self._dbcursor = self._dbconnection.cursor()
        self.close(False)

    def _connectdb(self, name: str):
        con = sqlite3.connect(name + '.db')
        print(f'connection to database {name} successful.')
        return con

    def close(self, status: bool):
        """
        Fechar a Conexão com o Banco de Dados.

        Ex.:
        db.close(True)
        """
        if status:
            self._dbcursor.close()
            self._dbconnection.close()
            print('Connection closed successfully.')

    def create_table(self, table_name: str, columns: str):
        """
        Criar uma Tabela no Banco de Dados.

        Args:
            table_name (str): Nome da Tabela.
            columns (str): Rótulos das Colunas.

        Ex.:
        db.create_table(
            table_name="usuarios",
            columns="nome, senha"
        )
        """
        if isinstance(table_name, str) and isinstance(columns, str):
            sqlstatement = (
                f"CREATE TABLE IF NOT EXISTS {table_name}\
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})"
            )
            self._dbcursor.execute(sqlstatement)
            self._dbconnection.commit()
            print(f'Table: {table_name}, created successfully.')
        else:
            print('ERROR')

    def insert_data(self, table_name: str, columns: list, values: list):
        """
        Inserir dados em uma Tabela do Banco de DAdos.

        Args:
            table_name (str): Nome da tabela.
            columns (list): Lista das colunas que serão inseridos dados.
            values (list): Lista dos valores que serão inseridos.

        Ex.:
        db.insert_data(
            table_name="usuarios",
            columns=['nome', 'senha'],
            values=[
                ['user1', 1234],
                ['user2', 4321]
            ]
        )
        """
        if (
            isinstance(table_name, str)
            and
            isinstance(columns, list)
            and
            isinstance(values, list)
        ):
            placeholders = ', '.join(['?' for _ in columns])
            unpacked_columns = ', '.join([i for i in columns])
            sqlstatement = f"INSERT INTO {table_name}\
                  (id, {unpacked_columns}) VALUES (NULL, {placeholders})"
            self._dbcursor.executemany(sqlstatement, values)
            self._dbconnection.commit()
            print('Successfully entered data.')
        else:
            print('ERROR')

    def select_data(self, columns: str, table_name: str):
        """
        Colsulte dados em uma tabela no banco de dados.

        Args:
            columns (str): Colunas da tabela.
            table_name (str): Nome da tabela.

        Ex.:
        db.select_data(
            columns="*",
            table_name="usuarios"
        )
        >>> list
        """
        if isinstance(columns, str) and isinstance(table_name, str):
            sqlstatement = f'SELECT {columns} FROM {table_name}'
            data = self._dbcursor.execute(sqlstatement)
            data_list = data.fetchall()
            print('Successfully selected data.')
            return data_list
        else:
            print('ERROR')

    def delete_data(self, table_name: str, condition: str):
        """
        Exclua dados em uma tabela no banco de dados.

        Args:
            table_name (str): Nome da tabela.
            condition (str): Condições dos dados a serem excluídos.

        Ex.:
        db.delete_data(
            table_name="usuarios",
            condition="nome='outro'"
        )
        """
        if isinstance(table_name, str) and isinstance(condition, str):
            sqlstatement = f'DELETE FROM {table_name} WHERE {condition}'
            self._dbcursor.execute(sqlstatement)
            self._dbconnection.commit()
            print('Successfully deleted data.')
        else:
            print('ERROR')

    def update_data(self, table_name: str, set: str, condition: str):
        """
        atualize dados em uma tabela no banco de dados.

        Args:
            table_name (str): Nome da tabela.
            set (str): Novos dados
            condition (str): Condição dos dados a serem atualizados.

        Ex.:
        db.delete_data(
            table_name="usuarios",
            set="senha=8766"
            condition="nome = 'User'"
        )
        """
        if (
            isinstance(table_name, str)
            and
            isinstance(set, str)
            and
            isinstance(condition, str)
        ):
            sqlstatement = f'UPDATE {table_name} SET {set} WHERE {condition}'
            self._dbcursor.execute(sqlstatement)
            self._dbconnection.commit()
            print('Successfully update data')
        else:
            print('ERROR')


if __name__ == "__main__":

    # Conexão com Banco de dados:
    db = Database('teste')

    # Criação de Tabelas:
    db.create_table(
        table_name='usuarios',
        columns='nome TEXT, senha INTEGER'
    )

    # Inserção dados:
    db.insert_data(
        table_name='usuarios',
        columns=['nome', 'senha'],
        values=[
            ['Everton', 1234],
            ['Milena', 4321],
            ['Outro', 6644]
        ]
    )

    # Atualização de dados
    db.update_data(
        table_name='usuarios',
        set='senha = 8766',
        condition='nome = "Everton"'
    )

    # Filtro/Consulta/Seleção de dados:
    table_usuarios = db.select_data(
        columns='*',
        table_name='usuarios'
    )

    print(table_usuarios)

    # Exclução de dados:
    db.delete_data(
        table_name='usuarios',
        condition='nome = "Outro"'
    )

    # Fechamento da conexão:
    db.close(True)
