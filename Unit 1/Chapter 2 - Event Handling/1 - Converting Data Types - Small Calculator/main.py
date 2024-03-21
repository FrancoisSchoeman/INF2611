# Page 50
# Event handling in PyQt is done using signals and slots.
# Every widget in PyQt has a set of predefined signals.
# Signals are emitted when a particular event occurs.
# Slots can be any callable function or method.

from PyQt5.QtWidgets import QDialog, QApplication
import sys
from ui import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButtonPlus.clicked.connect(self.addTwoNum)
        self.ui.pushButtonMinus.clicked.connect(self.minusTwoNum)
        self.ui.pushButtonTimes.clicked.connect(self.timesTwoNum)
        self.ui.pushButtonDivide.clicked.connect(self.divideTwoNum)

        self.show()

    def get_numbers(self):
        num1 = int(self.ui.lineEditOne.text()) if len(self.ui.lineEditOne.text()) > 0 else 0
        num2 = int(self.ui.lineEditTwo.text()) if len(self.ui.lineEditTwo.text()) > 0 else 0

        return num1, num2

    def addTwoNum(self):
        num1, num2 = self.get_numbers()
        result = num1 + num2
        self.ui.labelAnswer.setText(f"Answer: {result}")

    def minusTwoNum(self):
        num1, num2 = self.get_numbers()
        result = num1 - num2
        self.ui.labelAnswer.setText(f"Answer: {result}")

    def timesTwoNum(self):
        num1, num2 = self.get_numbers()
        result = num1 * num2
        self.ui.labelAnswer.setText(f"Answer: {result}")

    def divideTwoNum(self):
        num1, num2 = self.get_numbers()
        result = num1 / num2
        self.ui.labelAnswer.setText(f"Answer: {result}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyForm()
    window.show()

    sys.exit(app.exec_())