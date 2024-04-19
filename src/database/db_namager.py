from PySide6.QtSql import QSqlDatabase, QSqlQuery
import os


class DBManager:            # Создаем класс DBManager
    def __init__(self, db_path: str) -> None:       # При создании он будет принимать путь к базе
        self.db_path = db_path
        print(db_path, self.db_path)

    def check_base(self):                   # Функция проверки наличия файла базы данных
        exist = os.path.exists(self.db_path)
        print(f'Database exists = {exist}') # Контроль существования
        return exist

    def connect_to_base(self):              # Функция подключения к базе данных
        con = QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName(self.db_path)
        print(con.databaseName())           # Вывод в консоль для проверки подключения
        print(con.connectionName())
        print(f'Database is open = {con.open()}')       # Открываем базу данных
        if con.lastError().isValid():               # Если есть ошибки то выводим их в консоль
            print(f"Database error: {con.lastError().text()}")

    @staticmethod
    def execute_file(file_path: str):
        query = QSqlQuery()  # создаем новый запрос
        with open(file_path) as file:  # открываем файл
            rows = file.read().split(";")  # Читаем файл и разбиваем его на строки по знаку ;
            for row in rows:
                query.exec(row)  # Выполняем запросы

    def create_base(self, script_tables_path: str):  # создание БД
        self.execute_file(script_tables_path)

    def fill_init_data(self, script_data_path: str):        # Заполение первоначальныи данными
        self.execute_file(script_data_path)
