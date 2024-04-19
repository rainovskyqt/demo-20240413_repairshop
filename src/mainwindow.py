from PySide6.QtWidgets import QMainWindow
from PySide6.QtSql import QSqlDatabase
from ui.ui_mainwindow import Ui_MainWindow
from database.models import User


class MainWindow(QMainWindow):
    def __init__(self, user: User):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        '''
         При создании базы данных она создается одна на всю программу, но их может быть несколько, таким образом 
         мы получаем ссылку на глобальную базу, если в скобках указать имя подключения, то ссылка создастся на ту базу,
         сейчас нам это не нужно, но что бы понимать для чего тут self.database = QSqlDatabase.database() 
        '''
        self.database = QSqlDatabase.database()
