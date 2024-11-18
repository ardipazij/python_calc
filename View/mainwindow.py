# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

sys.path.append("../")
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QStandardItem, QFont
from ui_form import Ui_MainWindow
from calc import SmartCalculator
from numpy import arange
import json
from PIL import Image
from credit_window import CreditWindow
import logging
from logs import setup_logging
import configparser
import platform
from helper import is_float

logger = setup_logging(log_level=logging.INFO, rotation_period='d', interval=1)


def load_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        create_config(config_file)
    config.read(config_file)
    return config


def save_config(config, config_file='config.ini'):
    with open(config_file, 'w') as configfile:
        config.write(configfile)


def create_config(path='config.ini'):
    config = configparser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'current_size', '20')
    config.set('Settings', 'value_min_x', '-10')
    config.set('Settings', 'value_min_y', '-10')
    config.set('Settings', 'value_max_x', '10')
    config.set('Settings', 'value_max_y', '10')
    with open(path, 'w') as configfile:
        config.write(configfile)


class MainWindow(QMainWindow):
    max_value = 1000000
    min_value = -1000000
    min_size = 6
    max_size = 30

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.config = load_config()
        self.current_size = int(self.config.get('Settings', 'current_size', fallback='20'))
        self.value_min_x = int(self.config.get('Settings', 'value_min_x', fallback='-10'))
        self.value_min_y = int(self.config.get('Settings', 'value_min_y', fallback='-10'))
        self.value_max_x = int(self.config.get('Settings', 'value_max_x', fallback='10'))
        self.value_max_y = int(self.config.get('Settings', 'value_max_y', fallback='10'))
        self.upload_range_param()

        self.add_new_font_to_label()

        self.ui.pushButton_0.clicked.connect(self.digits_number)
        self.ui.pushButton_1.clicked.connect(self.digits_number)
        self.ui.pushButton_2.clicked.connect(self.digits_number)
        self.ui.pushButton_3.clicked.connect(self.digits_number)
        self.ui.pushButton_4.clicked.connect(self.digits_number)
        self.ui.pushButton_5.clicked.connect(self.digits_number)
        self.ui.pushButton_6.clicked.connect(self.digits_number)
        self.ui.pushButton_7.clicked.connect(self.digits_number)
        self.ui.pushButton_8.clicked.connect(self.digits_number)
        self.ui.pushButton_9.clicked.connect(self.digits_number)
        self.ui.pushButton_point.clicked.connect(self.digits_number)
        self.ui.pushButton_bracket_open.clicked.connect(self.digits_number)
        self.ui.pushButton_bracket_close.clicked.connect(self.digits_number)

        self.ui.pushButton_plus.clicked.connect(self.basic_operation)
        self.ui.pushButton_minus.clicked.connect(self.basic_operation)
        self.ui.pushButton_div.clicked.connect(self.basic_operation)
        self.ui.pushButton_mul.clicked.connect(self.basic_operation)
        self.ui.pushButton_exp.clicked.connect(self.basic_operation)
        self.ui.pushButton_mod.clicked.connect(self.basic_operation)

        self.ui.pushButton_log.clicked.connect(self.funcs)
        self.ui.pushButton_ln.clicked.connect(self.funcs)
        self.ui.pushButton_tan.clicked.connect(self.funcs)
        self.ui.pushButton_atan.clicked.connect(self.funcs)
        self.ui.pushButton_asin.clicked.connect(self.funcs)
        self.ui.pushButton_acos.clicked.connect(self.funcs)
        self.ui.pushButton_sin.clicked.connect(self.funcs)
        self.ui.pushButton_cos.clicked.connect(self.funcs)
        self.ui.pushButton_sqrt.clicked.connect(self.funcs)

        self.ui.pushButton_equal.clicked.connect(self.equal)

        self.ui.pushButton_delete_to_left_key.clicked.connect(self.delete_to_left_key)

        self.ui.pushButton_clear.clicked.connect(self.clear)

        self.ui.pushButton_e.clicked.connect(self.e_button)

        self.ui.pushButton_x.clicked.connect(self.x_logix)

        self.ui.pushButton_plot.clicked.connect(self.plot)

        self.ui.pushButton_clear_history.clicked.connect(self.clear_history)

        self.load_history()

        self.load_calculator_library()

        self.ui.pushButton_help.clicked.connect(self.open_help)

        self.ui.pushButton_credit.clicked.connect(self.open_credit)

        self.ui.pushButton_increase_font_size.clicked.connect(self.increase_font_size)
        self.ui.pushButton_decrease_font_size.clicked.connect(self.decrease_font_size)

        self.credit_window = 0

        self.show()

    def load_calculator_library(self):
        system = platform.system()
        if system == "Linux":
            lib_path = os.path.join(os.path.dirname(__file__), 'libs', 'linux_libcalc.so')
        elif system == "Windows":
            lib_path = os.path.join(os.path.dirname(__file__), 'libs', 'win_libcalc.dll')
        elif system == "Darwin":
            lib_path = os.path.join(os.path.dirname(__file__), 'libs', 'mac_libcalc.so')
        else:
            raise Exception("Unsupported platform")

        self.calculator = SmartCalculator(lib_path)

    def digits_number(self):
        sender = self.sender()
        current_text = self.ui.label.text()
        if self.check_string(current_text):
            current_text = sender.text()
        else:
            current_text += sender.text()
        self.ui.label.setText(current_text)

    @staticmethod
    def check_string(string):
        return (string == "0"
                or string == "Error"
                or string == "Maximum number of characters exceeded"
                or string == "Find two or more 'e' in number"
                or string == "Find two or more periods in number"
                or string == "Insufficient values for operation"
                or string == "Invalid argument"
                or string == "Out of range"
                or string == "Invalid token"
                or string == "Invalid value encountered"
                or string == "Evaluation error")

    def basic_operation(self):
        sender = self.sender()
        current_text = self.ui.label.text()
        if self.check_string(current_text):
            current_text = sender.text()
        else:
            current_text += sender.text()
        self.ui.label.setText(current_text)

    def funcs(self):
        sender = self.sender()
        current_text = self.ui.label.text()
        if self.check_string(current_text):
            current_text = sender.text() + '('
        else:
            current_text += sender.text() + '('
        self.ui.label.setText(current_text)

    def delete_to_left_key(self):
        current_text = self.ui.label.text()

        if not self.check_string(current_text):

            functions = ["atan(", "asin(", "acos(", "sin(", "cos(", "tan(", "log(", "ln(", "sqrt("]

            function_found = False
            for func in functions:
                if current_text.endswith(func):
                    current_text = current_text[:-len(func)]
                    function_found = True
                    break

            if not function_found:
                current_text = current_text[:-1]

            self.ui.label.setText(current_text)

    def clear(self):
        self.ui.label.setText("0")

    def e_button(self):
        sender = self.sender()
        last_char = self.ui.label.text()[-1]
        if last_char != 'x' and last_char.isdigit() and last_char != '.' and last_char != ')':
            self.ui.label.setText(self.ui.label.text() + sender.text())

    def equal(self):
        input_expression = self.ui.label.text()
        x = self.ui.line_x.text()
        is_x_number = x.isdigit()
        self.calculator.set_expression(input_expression)
        self.add_button(self.ui.label.text())
        logger.info(f"Вычисление: {input_expression}, x = {x}")
        if is_x_number:
            result = self.calculator.get_result(is_x_number, float(x))
        else:
            result = self.calculator.get_result()
        if (is_float(result)):
            logger.info(f"Результат: {result}")
        else:
            logger.error(f"Ошибка: {result}")
        self.ui.label.setText(str(result))

    def x_logix(self):
        current_text = self.ui.label.text()
        last_char = self.ui.label.text()[-1]
        if self.check_string(current_text):
            self.ui.label.setText("x")
        elif (last_char != 'x' and not last_char.isdigit() and last_char != '.' and
              last_char != ')' and last_char != 'e'):
            self.ui.label.setText(current_text + 'x')

    def plot(self):
        logger.info(f"Отображение графика функции: {self.ui.label.text()}")
        if not (is_float(self.ui.line_x_min.text())
                and is_float(self.ui.line_x_max_2.text())
                and is_float(self.ui.line_y_min_2.text())
                and is_float(self.ui.line_y_max_2.text())):
            self.ui.label.setText("Error")
            logger.error(f"Ошибка при отображении графика: input_error - в границах диапазона ожидались цифры")
            return

        x_min = int(self.ui.line_x_min.text())
        x_max = int(self.ui.line_x_max_2.text())
        y_min = int(self.ui.line_y_min_2.text())
        y_max = int(self.ui.line_y_max_2.text())

        if (self.min_value < x_min < x_max < self.max_value
                and self.min_value < y_min < y_max < self.max_value):

            h = min(abs(x_max - x_min) / 10000, abs(y_max - y_min) / 10000)
            y, x = [], []
            current_text = self.ui.label.text()
            self.calculator.set_expression(current_text)

            for X in arange(x_min, x_max, h):
                result = self.calculator.get_result(1, X)
                if isinstance(result, (int, float)):
                    y.append(float(result))
                    x.append(X)

            self.ui.graphics_view.clear()
            self.ui.graphics_view.plot(x, y)
            logger.info(f"График успешно построен")

        else:
            self.ui.label.setText("Error")
            logger.error(
                f"Ошибка при отображении графика: input_error - в границах отображения диапазона ожидались числа от -1000000 до 1000000")

    def history(self):
        sender = self.sender()
        current_text = sender.text()
        self.ui.label.setText(current_text)

    def add_button(self, text):
        if not self.check_string(text):
            button = QPushButton(text)
            button.clicked.connect(self.history)
            item = QStandardItem()
            item.setSizeHint(button.sizeHint())
            self.ui.model.insertRow(0, item)
            self.ui.listView.setIndexWidget(self.ui.model.index(0, 0), button)

    def clear_history(self):
        self.ui.model.clear()

    def load_history(self):
        try:
            with open("history.json", "r") as file:
                history = json.load(file)
            for text in reversed(history):
                self.add_button(text)
        except FileNotFoundError:
            pass

    def save_history(self):
        history = []
        for row in range(self.ui.model.rowCount()):
            index = self.ui.model.index(row, 0)
            button = self.ui.listView.indexWidget(index)
            history.append(button.text())

        with open("history.json", "w") as file:
            json.dump(history, file)
        self.config.set('Settings', 'current_size', str(self.current_size))
        self.config.set('Settings', 'value_min_x', self.ui.line_x_min.text())
        self.config.set('Settings', 'value_max_x', self.ui.line_x_max_2.text())
        self.config.set('Settings', 'value_min_y', self.ui.line_y_min_2.text())
        self.config.set('Settings', 'value_max_y', self.ui.line_y_max_2.text())
        save_config(self.config)

    @staticmethod
    def open_help():
        try:
            help_path = os.path.join(os.path.dirname(__file__), 'help.png')
            os.system(f'open "{help_path}"')
        except:
            try:
                help_path = os.path.join(os.path.dirname(__file__), 'help.png')
                os.system(f'xdg-open "{help_path}"')
            except:
                try:
                    help_path = os.path.join(os.path.dirname(__file__), 'help.png')
                    os.system(f'gnome-open "{help_path}"')
                except:
                    img = Image.open(os.path.join(os.path.dirname(__file__), 'help.png'))
                    img.show()

    def open_credit(self):
        self.credit_window = CreditWindow()

    def add_new_font_to_label(self):
        font = QFont()
        font.setPointSize(self.current_size)
        self.ui.label.setFont(font)

    def increase_font_size(self):
        current_font = self.ui.label.font()
        current_size = current_font.pointSize()
        new_size = current_size + 2
        if new_size < self.max_size:
            self.current_size = new_size
            self.add_new_font_to_label()

    def decrease_font_size(self):
        current_font = self.ui.label.font()
        current_size = current_font.pointSize()
        new_size = current_size - 2
        if new_size > self.min_size:
            self.current_size = new_size
            self.add_new_font_to_label()

    def upload_range_param(self):
        self.ui.line_x_min.setText(str(self.value_min_x))
        self.ui.line_y_min_2.setText(str(self.value_min_y))
        self.ui.line_x_max_2.setText(str(self.value_max_x))
        self.ui.line_y_max_2.setText(str(self.value_max_y))


if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    app.aboutToQuit.connect(widget.save_history)
    sys.exit(app.exec())
