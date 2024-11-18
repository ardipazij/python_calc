from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from credit_calc import CreditCalc
from credit_ui import Ui_credit_window
from helper import is_float
import platform
import os

class CreditWindow(QMainWindow):

    def __init__(self):
        super(CreditWindow, self).__init__()
        self.ui = Ui_credit_window()
        self.ui.setupUi(self)
        self.load_calculator_library()
        self.ui.pushButton_calculate.clicked.connect(self.on_pushButton_calculate_clicked)
        self.show()

    def load_calculator_library(self):
        system = platform.system()
        if system == "Linux":
            lib_path = os.path.join(os.path.dirname(__file__), 'libs', 'linux_libcredit.so')
        elif system == "Windows":
            lib_path = os.path.join(os.path.dirname(__file__), 'libs', 'win_libcredit.dll')
        elif system == "Darwin":
            lib_path = os.path.join(os.path.dirname(__file__), 'libs', 'mac_libcredit.so')
        else:
            raise Exception("Unsupported platform")

        self.credit_calculator = CreditCalc(lib_path)

    def on_pushButton_calculate_clicked(self):
        percents = self.ui.lineEdit_percents.text()
        summa = self.ui.lineEdit_sum.text()
        months = self.ui.lineEdit_months.text()
        percents_validate = is_float(percents)
        sum_validate = is_float(summa)
        months_validate = is_float(months)

        if months_validate:
            months = float(months) * 12 if self.ui.comboBox_type_date.currentText() == 'Лет' else float(months)
        if (not percents_validate
                or not sum_validate
                or not months_validate
                or float(percents) < 0.01
                or float(percents) > 999
                or months <= 0
                or months > 600
                or float(summa) <= 0):
            self.ui.textEdit.clear()
            self.ui.textEdit.append('Error')
            self.ui.label_7_percents.setText('Error')
            self.ui.label_7_result.setText('Error')
            return

        if self.ui.radioButton.isChecked():
            result = self.credit_calculator.calculate_ann(float(percents), months, float(summa))
            self.ui.textEdit.clear()
            self.ui.textEdit.append(str(result[2]))
            self.ui.label_7_percents.setNum(result[1])
            self.ui.label_7_result.setNum(result[0])
        elif self.ui.radioButton_2.isChecked():
            self.ui.textEdit.clear()
            result = self.credit_calculator.calculate_diff(float(percents), months, float(summa))
            for k in range(result[2]):
                self.ui.textEdit.append(f'{k + 1}. {result[3][k]}')
            self.ui.label_7_percents.setNum(result[1])
            self.ui.label_7_result.setNum(result[0])
