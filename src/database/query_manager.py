from PySide6.QtSql import QSqlQuery
from .db_namager import DBManager
from .models import User, Order, Dictionary


class QueryManager:
    def __init__(self, database: DBManager):
        self.base = database

    @staticmethod
    def execute_query(query_row: str, params=None):            # функция выполнения запроса
        if params is None:
            params = {}
        query = QSqlQuery()
        query.prepare(query_row)                                # Подготовка запроса из параметра query_row

        for key, value in params.items():                       # Подстановка значений для запроса
            query.bindValue(key, value)

        query.exec()                                            # Выполнение запроса

        if query.lastError().isValid():                          # В случае ошибки выводим сообщение
            print(f'Query error: {query.lastError().text()}')

        return query

    def check_login(self, login: str, password: str):
        query_string = "SELECT id, name, post_id FROM users WHERE login = :login AND password = :password"
        params = {":login": login, ":password":  password}

        answer = self.execute_query(query_string, params)
        if answer.next():
            user = User(answer.value("id"), answer.value("name"), answer.value("post_id"))
            return user
        else:
            return 0

    def get_users(self):
        query_string = """SELECT U.id as id, U.name as name, U.login as login, U.post_id as post_id, P.name as post_name   
                          FROM users
                          INNER JOIN posts P ON U.post_id = P.id """
        answer = self.execute_query(query_string)
        users = []
        while answer.next():
            users.append(User(answer.value("id"),
                              answer.value("name"),
                              answer.value("post_id"),
                              answer.value("post_name")))
        return users

    def delete_order(self, order_id: int):
        query_string = "DELETE FROM orders WHERE id = :id"
        self.execute_query(query_string, {":id": order_id})

    def get_order(self, order_id: int):
        query_string = """ SELECT add_date, resolve_date, equipment_id, fault_id, description, client_id, 
        status_id, worker_id
        FROM orders
        WHERE id = :order_id
        """
        answer = self.execute_query(query_string, {":order_id": order_id})
        if answer.next():
            order = Order(
                answer.value("add_date"),
                answer.value("resolve_date"),
                answer.value("equipment_id"),
                answer.value("fault_id"),
                answer.value("description"),
                answer.value("client_id"),
                answer.value("status_id"),
                answer.value("worker_id")
            )
            return order
        else:
            return 0

    def get_dictionary(self, table: str):
        query_string = f"SELECT id, mane FROM {table}"
        answer = self.execute_query(query_string)
        if answer.next():
            return Dictionary(answer.value("id"), answer.value("name"))

    def get_equipment(self):
        return self.get_dictionary("equipment")

    def get_fault(self):
        return self.get_dictionary("fault")

    def get_status(self):
        return self.get_dictionary("status")