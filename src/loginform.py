from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_loginform import Ui_dialog
from database.db_namager import DBManager
from settings import DB_PATH, TABLE_SCRIPT_PATH, DATA_SCRIPT_PATH
from database.query_manager import QueryManager
from database.models import User
from mainwindow import MainWindow


class LoginForm(QDialog):
    main_window: MainWindow

    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.database = self.init_base()
        self.query = QueryManager(self.database)
        self.init_connections()

    def init_connections(self):
        self.ui.btn_cancel.clicked.connect(self.exit)
        self.ui.btn_ok.clicked.connect(self.login)

    @staticmethod
    def init_base():
        database = DBManager(DB_PATH)
        base_exists = database.check_base()
        database.connect_to_base()
        if not base_exists:
            database.create_base(TABLE_SCRIPT_PATH)
            database.fill_init_data(DATA_SCRIPT_PATH)
        return database

    def login(self):
        user = self.query.check_login(self.ui.line_login.text(), self.ui.line_password.text())
        if not user:
            self.login_incorrect()
            return
        else:
            self.start_main_window(user)

    def login_incorrect(self):
        QMessageBox.critical(self, "Неудача", "Неверный логин или пароль")

    def start_main_window(self, user: User):
        self.main_window = MainWindow(user)
        self.main_window.show()
        self.close()

    def exit(self):
        self.close()
