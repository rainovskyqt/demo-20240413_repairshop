from PySide6.QtWidgets import QApplication
from src.loginform import LoginForm

if __name__ == '__main__':
    app = QApplication()
    login_form = LoginForm()
    login_form.show()
    app.exec()

