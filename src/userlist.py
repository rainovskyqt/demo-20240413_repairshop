from PySide6.QtWidgets import QDialog, QMessageBox

from database.query_manager import QueryManager
from ui.ui_userlist import Ui_UserList


class UserList(QDialog):
    def __init__(self, database):
        super(UserList, self).__init__()
        self.ui = Ui_UserList()
        self.ui.setupUi(self)
        self.query = QueryManager(database)

    def load_users(self):
        users = self.query.get_users()
        for user in users:
            pass
