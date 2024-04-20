from PySide6.QtWidgets import QDialog
from ui.ui_order_edit import Ui_EditOrder


class EditOrder(QDialog):
    def __init__(self):
        super(EditOrder, self).__init__()
        self.ui = Ui_EditOrder()
        self.ui.setupUi(self)
