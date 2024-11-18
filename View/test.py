import unittest
from PySide6.QtWidgets import QApplication
from PySide6.QtTest import QTest
from PySide6.QtCore import Qt
from mainwindow import MainWindow


class TestMainWindow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])
        cls.widget = MainWindow()

    @classmethod
    def tearDownClass(cls):
        cls.widget.close()
        cls.app.quit()

    def setUp(self):
        self.widget.ui.label.setText("0")
        self.widget.ui.model.clear()

    def test_digits_number(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "1")

    def test_basic_operation(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_plus, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_2, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "1+2")

    def test_funcs(self):
        QTest.mouseClick(self.widget.ui.pushButton_sin, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "sin(")

    def test_delete_to_left_key(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_2, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_delete_to_left_key, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "1")

    def test_clear(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_clear, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "0")

    def test_e_button(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_e, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "1e")

    def test_equal(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_plus, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_2, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_equal, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "3.0")

    def test_x_logix(self):
        QTest.mouseClick(self.widget.ui.pushButton_x, Qt.LeftButton)
        self.assertEqual(self.widget.ui.label.text(), "x")

    def test_plot(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_x, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_plot, Qt.LeftButton)
        self.assertNotEqual(self.widget.ui.label.text(), "Error")

    def test_clear_history(self):
        QTest.mouseClick(self.widget.ui.pushButton_1, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_equal, Qt.LeftButton)
        QTest.mouseClick(self.widget.ui.pushButton_clear_history, Qt.LeftButton)
        self.assertEqual(self.widget.ui.model.rowCount(), 0)


if __name__ == '__main__':
    unittest.main()
