# A Dialog application contains buttons. It doesn't contain a menu bar, a status bar, or a toolbar or a central widget.
# A Main Window apllication contains all of these.

# There are two types of dialogs:
# 1. Modal Dialogs: These dialogs block the user from interacting with the parent window until the dialog is closed.
# 2. Modeless Dialogs: These dialogs are independent of the parent window. They don't block the user from interacting with the parent window.

# The menu on the left within Qt Designer is called the widget box. It contains all the widgets that can be added to the form.

# Event handling in PyQt5 uses signals and slots. A signal is an event, and a slot is a method that is executed on the occurrence of a signal.

from ui import *
from PyQt5.QtWidgets import QDialog, QApplication
import sys

# p35


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.dispMessage)
        self.show()

    def dispMessage(self):
        self.ui.label_2.setText("Hello " + self.ui.lineEditName.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
