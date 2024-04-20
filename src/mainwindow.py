from PySide6.QtCore import QSortFilterProxyModel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation
from ui.ui_mainwindow import Ui_MainWindow
from database.models import User
from .database.query_manager import QueryManager
from .order_edit import EditOrder

class MainWindow(QMainWindow):
    def __init__(self, user: User, login_form):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user = user
        self.login_form = login_form
        '''
         При создании базы данных она создается одна на всю программу, но их может быть несколько, таким образом 
         мы получаем ссылку на глобальную базу, если в скобках указать имя подключения, то ссылка создастся на ту базу,
         сейчас нам это не нужно, но что бы понимать для чего тут self.database = QSqlDatabase.database() 
        '''
        self.database = QSqlDatabase.database()
        self.query_manager = QueryManager(self.database)
        self.sql_model = QSqlRelationalTableModel(self, self.database)
        self.proxy_model = QSortFilterProxyModel(self)
        self.proxy_model.setSourceModel(self.sql_model)
        self.ui.tv_orders.setModel(self.proxy_model)
        self.init_connections()
        self.set_table()
        self.select_orders()
        self.order_editor = EditOrder(1, self.query_manager)

    def exit(self):
        self.login_form.show()
        self.close()

    def set_table(self):            # устанавливаем связи с таблицами
        # Устанавливаем таблицу из которой наша модель будет получать данные
        self.sql_model.setTable("orders")
        # Устанавливаем связи с таблицами на которые ссылаются внешние ключи
        # self.sql_model.setRelation(номер колонки внешнего ключа, QSqlRelation("название внешней таблицы", "поле ключа", "поле котрое поставитьь из внешней таблицы"))
        self.sql_model.setRelation(3, QSqlRelation("equipment", "id", "name"))
        self.sql_model.setRelation(4, QSqlRelation("fault", "id", "name"))
        self.sql_model.setRelation(6, QSqlRelation("clients", "id", "name"))
        self.sql_model.setRelation(7, QSqlRelation("status", "id", "name"))
        self.sql_model.setRelation(8, QSqlRelation("users", "id", "name"))

        self.ui.tv_orders.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.ui.tv_orders.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.tv_orders.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

    def select_orders(self):
        self.sql_model.select()     # Вызов выборки из базы
        # Установка заголовков таблицы показывающей данные
        self.sql_model.setHeaderData(0, Qt.Orientation.Horizontal, "№ заявки")
        self.sql_model.setHeaderData(1, Qt.Orientation.Horizontal, "Дата получения")
        self.sql_model.setHeaderData(2, Qt.Orientation.Horizontal, "Дака выполнения")
        self.sql_model.setHeaderData(3, Qt.Orientation.Horizontal, "Оборудование")
        self.sql_model.setHeaderData(4, Qt.Orientation.Horizontal, "Тип неисправности")
        self.sql_model.setHeaderData(6, Qt.Orientation.Horizontal, "Клиент")
        self.sql_model.setHeaderData(7, Qt.Orientation.Horizontal, "Статус")
        self.sql_model.setHeaderData(8, Qt.Orientation.Horizontal, "Исполнитель")

        self.ui.tv_orders.setColumnHidden(5, True)      # прячем колонку с описанием, она нам на главной форме не нужна
        self.ui.tv_orders.resizeColumnsToContents()     # Установка столбцов по ширине данных

    def edit_order(self):
        rec_id = self.get_current_record_id()
        if not rec_id:
            return
        print(f" Editable order id = {rec_id}")
        # editor = EditOrder(rec_id, self.query_manager)
        # editor.show()
        self.order_editor.show()

    def get_current_record_id(self):
        if not self.ui.tv_orders.selectedIndexes()[0]:
            return 0
        row = self.ui.tv_orders.selectedIndexes()[0].row()
        record_id = self.proxy_model.data(self.proxy_model.index(row, 0))
        return record_id

    def init_connections(self):
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.tv_orders.doubleClicked.connect(self.edit_order)
        self.ui.btn_edit.clicked.connect(self.edit_order)
        self.ui.btn_delete.clicked.connect(self.delete_record)

    def delete_record(self):
        rec_id = self.get_current_record_id()
        if not rec_id:
            return

        answer = QMessageBox.question(self, "Удаление записи", f"Удалить заказ {rec_id}?")
        if answer == QMessageBox.StandardButton.No:
            return

        self.query_manager.delete_order(rec_id)
        self.select_orders()
