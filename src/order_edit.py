from PySide6.QtWidgets import QDialog, QComboBox
from ui.ui_order_edit import Ui_EditOrder
from database.query_manager import QueryManager
from database.models import Order, Dictionary
from datetime import date


class EditOrder(QDialog):
    def __init__(self, order_id: int, query_manager: QueryManager):
        super(EditOrder, self).__init__()
        self.ui = Ui_EditOrder()
        self.ui.setupUi(self)
        self.order_id = order_id
        self.query_manager = query_manager
        self.load_dict()
        self.to_form(self.order_id)

    def get_order_data(self, order_id):
        # Если order_id не 0, значит мы перезали заказ для
        # редктирования и получаем его из базы
        if order_id:
            return self.query_manager.get_order(order_id)
        else:
            # Иначе это новый заказ и мы создаем пустой
            return Order(date.today().strftime("%d.%m.%y"))

    def load_dict(self):            # Загружаем стправочники
        equipment = self.query_manager.get_equipment()
        self.set_dict(equipment, self.ui.cb_equipment)

        fault = self.query_manager.get_fault()
        self.set_dict(fault, self.ui.cb_fault)

        status = self.query_manager.get_status()
        self.set_dict(status, self.ui.cb_status)

    def set_dict(self, vals: Dictionary, box: QComboBox):             # устанавливаем стправочники на форму
        box.clear()                 # обязательно сначала очищаем содержимое
        box.addItem("-", 0)           # добавляем пустое значение
        for row in vals:
            box.addItem(row.name, row.id)

    def to_form(self, order_id):
        order = self.get_order_data(order_id)
