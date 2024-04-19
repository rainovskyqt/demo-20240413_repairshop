# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userlist.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_UserList(object):
    def setupUi(self, UserList):
        if not UserList.objectName():
            UserList.setObjectName(u"UserList")
        UserList.resize(791, 571)
        self.verticalLayout_2 = QVBoxLayout(UserList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(UserList)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.line_login = QLineEdit(UserList)
        self.line_login.setObjectName(u"line_login")

        self.gridLayout.addWidget(self.line_login, 0, 1, 1, 1)

        self.label_2 = QLabel(UserList)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)

        self.line_password = QLineEdit(UserList)
        self.line_password.setObjectName(u"line_password")

        self.gridLayout.addWidget(self.line_password, 0, 3, 1, 1)

        self.label_3 = QLabel(UserList)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.line_password_2 = QLineEdit(UserList)
        self.line_password_2.setObjectName(u"line_password_2")

        self.gridLayout.addWidget(self.line_password_2, 1, 1, 1, 1)

        self.label_4 = QLabel(UserList)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.cb_post = QComboBox(UserList)
        self.cb_post.setObjectName(u"cb_post")

        self.gridLayout.addWidget(self.cb_post, 1, 3, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.bnt_save = QPushButton(UserList)
        self.bnt_save.setObjectName(u"bnt_save")

        self.horizontalLayout.addWidget(self.bnt_save)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tw_user_list = QTableWidget(UserList)
        if (self.tw_user_list.columnCount() < 4):
            self.tw_user_list.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tw_user_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tw_user_list.setObjectName(u"tw_user_list")
        self.tw_user_list.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.tw_user_list)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_2 = QPushButton(UserList)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.retranslateUi(UserList)

        QMetaObject.connectSlotsByName(UserList)
    # setupUi

    def retranslateUi(self, UserList):
        UserList.setWindowTitle(QCoreApplication.translate("UserList", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.label.setText(QCoreApplication.translate("UserList", u"\u043b\u043e\u0433\u0438\u043d", None))
        self.label_2.setText(QCoreApplication.translate("UserList", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_3.setText(QCoreApplication.translate("UserList", u"\u0418\u043c\u044f", None))
        self.label_4.setText(QCoreApplication.translate("UserList", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.bnt_save.setText(QCoreApplication.translate("UserList", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        ___qtablewidgetitem = self.tw_user_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UserList", u"\u041d\u043e\u043c\u0435\u0440", None));
        ___qtablewidgetitem1 = self.tw_user_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UserList", u"\u041b\u043e\u0433\u0438\u043d", None));
        ___qtablewidgetitem2 = self.tw_user_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("UserList", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c", None));
        ___qtablewidgetitem3 = self.tw_user_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("UserList", u"\u0418\u043c\u044f", None));
        self.pushButton_2.setText(QCoreApplication.translate("UserList", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

