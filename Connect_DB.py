import pyodbc

# Класс DataBase отвечает за подключение к базе данных и дальнейшее с ней взаимодействие.
class DataBase:
    # В конструкторе класса создается подключение к базе данных.
    def __init__(self):
        super().__init__()

        self.connect = pyodbc.connect(
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=./Database11(1).accdb;'
        )
        self.cursor = self.connect.cursor()

    # Получает все колонки: columns="*", из таблицы, название её содержится в nameTable, по определённому условию.
    def select(self, columns="*", nameTable="", condition_select=" where "):
        self.cursor.execute(f'''select {columns} from [{nameTable}]{condition_select}''')
        result = self.cursor.fetchall()

        return result

    # Обновление данных в таблице.
    def update(self, nameTable="", columns_val="", condition_update="", values=[]):
        query = f'''update [{nameTable}] set {columns_val} where {condition_update}'''
        self.cursor.execute(query, tuple(values))
        self.connect.commit()

    # Добавление данных в таблицу.
    def insert(self, nameTable="", nameColumn="", valueColumn=()):
        params = ", ".join(["?" for _ in range(len(valueColumn))])
        query = f"INSERT INTO [{nameTable}] ({nameColumn}) VALUES ({params})"
        self.cursor.execute(query, valueColumn)
        self.connect.commit()

    # Удаление данных в таблице.
    def delete(self, nameTable="", condition_delete="", value=1):
        query = f'''delete from [{nameTable}] where {condition_delete}'''
        self.cursor.execute(query, value)
        self.connect.commit()

    # Получение пользовательских запросов из БД.
    def get_queries(self):
        query = "SELECT Name FROM MSysObjects_Copy WHERE Type = 5"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    # Выполнение пользовательского запроса.
    def execute_query(self, query_name, parameter=""):
        query = f"EXEC [{query_name}] {parameter}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
