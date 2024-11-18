# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credit.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QRadioButton,
                               QSizePolicy, QStatusBar, QTextEdit, QWidget)


class Ui_credit_window(object):
    def setupUi(self, credit_window):
        if not credit_window.objectName():
            credit_window.setObjectName(u"credit_window")
        credit_window.resize(514, 431)
        self.centralwidget = QWidget(credit_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_price_info = QLabel(self.centralwidget)
        self.label_price_info.setObjectName(u"label_price_info")
        self.label_price_info.setGeometry(QRect(20, 0, 91, 71))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 60, 101, 51))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 91, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 110, 58, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 210, 101, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 250, 91, 51))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 310, 111, 31))
        self.label_7_montly_pay = QLabel(self.centralwidget)
        self.label_7_montly_pay.setObjectName(u"label_7_montly_pay")
        self.label_7_montly_pay.setGeometry(QRect(160, 220, 341, 21))
        self.label_7_percents = QLabel(self.centralwidget)
        self.label_7_percents.setObjectName(u"label_7_percents")
        self.label_7_percents.setGeometry(QRect(160, 260, 341, 21))
        self.label_7_result = QLabel(self.centralwidget)
        self.label_7_result.setObjectName(u"label_7_result")
        self.label_7_result.setGeometry(QRect(160, 320, 341, 16))
        self.comboBox_type_date = QComboBox(self.centralwidget)
        self.comboBox_type_date.addItem("")
        self.comboBox_type_date.addItem("")
        self.comboBox_type_date.setObjectName(u"comboBox_type_date")
        self.comboBox_type_date.setGeometry(QRect(410, 70, 103, 32))
        self.pushButton_calculate = QPushButton(self.centralwidget)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")
        self.pushButton_calculate.setGeometry(QRect(200, 350, 100, 32))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 160, 111, 31))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(140, 160, 171, 31))
        self.lineEdit_percents = QLineEdit(self.centralwidget)
        self.lineEdit_percents.setObjectName(u"lineEdit_percents")
        self.lineEdit_percents.setGeometry(QRect(130, 110, 113, 31))
        self.lineEdit_sum = QLineEdit(self.centralwidget)
        self.lineEdit_sum.setObjectName(u"lineEdit_sum")
        self.lineEdit_sum.setGeometry(QRect(130, 20, 381, 31))
        self.lineEdit_months = QLineEdit(self.centralwidget)
        self.lineEdit_months.setObjectName(u"lineEdit_months")
        self.lineEdit_months.setGeometry(QRect(130, 70, 281, 31))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 210, 351, 31))
        credit_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(credit_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 514, 24))
        credit_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(credit_window)
        self.statusbar.setObjectName(u"statusbar")
        credit_window.setStatusBar(self.statusbar)

        self.retranslateUi(credit_window)

        QMetaObject.connectSlotsByName(credit_window)

    # setupUi

    def retranslateUi(self, credit_window):
        credit_window.setWindowTitle(QCoreApplication.translate("credit_window", u"MainWindow", None))
        self.label_price_info.setText(QCoreApplication.translate("credit_window",
                                                                 u"\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430\n"
                                                                 "\u043a\u0440\u0435\u0434\u0438\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("credit_window",
                                                      u"\u0421\u0440\u043e\u043a \u043a\u0440\u0435\u0434\u0438\u0442\u0430",
                                                      None))
        self.label_2.setText(QCoreApplication.translate("credit_window",
                                                        u"\u041f\u0440\u043e\u0446\u0435\u043d\u0442\u043d\u0430\u044f\n"
                                                        "\u0441\u0442\u0430\u0432\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("credit_window", u"%", None))
        self.label_4.setText(QCoreApplication.translate("credit_window",
                                                        u"\u0415\u0436\u0435\u043c\u0435\u0441\u044f\u0447\u043d\u044b\u0439\n"
                                                        "\u043f\u043b\u0430\u0442\u0435\u0436", None))
        self.label_5.setText(QCoreApplication.translate("credit_window",
                                                        u"\u041d\u0430\u0447\u0438\u0441\u043b\u0435\u043d\u043d\u044b\u0435\n"
                                                        "\u043f\u0440\u043e\u0446\u0435\u043d\u0442\u044b", None))
        self.label_6.setText(QCoreApplication.translate("credit_window",
                                                        u"\u0414\u043e\u043b\u0433 + \u043f\u0440\u043e\u0446\u0435\u043d\u0442\u044b",
                                                        None))
        self.label_7_montly_pay.setText("")
        self.label_7_percents.setText("")
        self.label_7_result.setText("")
        self.comboBox_type_date.setItemText(0, QCoreApplication.translate("credit_window",
                                                                          u"\u041c\u0435\u0441\u044f\u0446\u0435\u0432",
                                                                          None))
        self.comboBox_type_date.setItemText(1, QCoreApplication.translate("credit_window", u"\u041b\u0435\u0442", None))

        self.pushButton_calculate.setText(QCoreApplication.translate("credit_window", u"Calculate", None))
        self.radioButton.setText(QCoreApplication.translate("credit_window",
                                                            u"\u0410\u043d\u043d\u0443\u0438\u0442\u0435\u0442\u043d\u044b\u0435",
                                                            None))
        self.radioButton_2.setText(QCoreApplication.translate("credit_window",
                                                              u"\u0414\u0438\u0444\u0444\u0435\u0440\u0435\u043d\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0435",
                                                              None))
    # retranslateUi
