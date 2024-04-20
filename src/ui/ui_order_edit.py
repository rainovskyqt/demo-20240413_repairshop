# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_edit.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_EditOrder(object):
    def setupUi(self, EditOrder):
        if not EditOrder.objectName():
            EditOrder.setObjectName(u"EditOrder")
        EditOrder.resize(698, 446)
        self.verticalLayout = QVBoxLayout(EditOrder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(EditOrder)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.date_add_date = QDateEdit(EditOrder)
        self.date_add_date.setObjectName(u"date_add_date")

        self.horizontalLayout.addWidget(self.date_add_date)

        self.label_2 = QLabel(EditOrder)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.date_complite_date = QDateEdit(EditOrder)
        self.date_complite_date.setObjectName(u"date_complite_date")

        self.horizontalLayout.addWidget(self.date_complite_date)

        self.label_3 = QLabel(EditOrder)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.cb_equipment = QComboBox(EditOrder)
        self.cb_equipment.setObjectName(u"cb_equipment")

        self.horizontalLayout.addWidget(self.cb_equipment)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(EditOrder)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.cb_fault = QComboBox(EditOrder)
        self.cb_fault.setObjectName(u"cb_fault")

        self.horizontalLayout_2.addWidget(self.cb_fault)

        self.label_5 = QLabel(EditOrder)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_2.addWidget(self.label_5)

        self.cb_client = QComboBox(EditOrder)
        self.cb_client.setObjectName(u"cb_client")

        self.horizontalLayout_2.addWidget(self.cb_client)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(EditOrder)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.cb_status = QComboBox(EditOrder)
        self.cb_status.setObjectName(u"cb_status")

        self.horizontalLayout_3.addWidget(self.cb_status)

        self.label_7 = QLabel(EditOrder)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.cb_employeer = QComboBox(EditOrder)
        self.cb_employeer.setObjectName(u"cb_employeer")

        self.horizontalLayout_3.addWidget(self.cb_employeer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.text_description = QPlainTextEdit(EditOrder)
        self.text_description.setObjectName(u"text_description")

        self.verticalLayout.addWidget(self.text_description)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(EditOrder)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_4.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(EditOrder)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_4.addWidget(self.btn_cancel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(EditOrder)

        QMetaObject.connectSlotsByName(EditOrder)
    # setupUi

    def retranslateUi(self, EditOrder):
        EditOrder.setWindowTitle(QCoreApplication.translate("EditOrder", u"\u0420\u0430\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label.setText(QCoreApplication.translate("EditOrder", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("EditOrder", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("EditOrder", u"\u041e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("EditOrder", u"\u0442\u0438\u043f \u043d\u0435\u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e\u0441\u0442\u0438", None))
        self.label_5.setText(QCoreApplication.translate("EditOrder", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_6.setText(QCoreApplication.translate("EditOrder", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.label_7.setText(QCoreApplication.translate("EditOrder", u"\u0418\u0441\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c", None))
        self.btn_save.setText(QCoreApplication.translate("EditOrder", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("EditOrder", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

