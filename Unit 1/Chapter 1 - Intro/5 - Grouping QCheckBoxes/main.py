# There are many ways to group inputs or buttons in a GUI.
# One way is the use the GroupBox widget. This widget is a container that groups a set of widgets together.

import sys
from PyQt5.QtWidgets import QDialog, QApplication

from ui import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.checkBoxChoclateAlmond.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxChoclateChips.stateChanged.connect(self.dispAmount)

        self.ui.checkBoxCookieDough.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxRockyRoad.stateChanged.connect(self.dispAmount)
        
        self.ui.checkBoxCoffee.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSoda.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxTea.stateChanged.connect(self.dispAmount)

        self.show()


    def dispAmount(self):
        amount = 0
        if self.ui.checkBoxChoclateAlmond.isChecked():
            amount = amount + 3
        if self.ui.checkBoxChoclateChips.isChecked():
            amount = amount + 4
        if self.ui.checkBoxCookieDough.isChecked():
            amount = amount + 2
        if self.ui.checkBoxRockyRoad.isChecked():
            amount = amount + 5
        if self.ui.checkBoxCoffee.isChecked():
            amount = amount + 2
        if self.ui.checkBoxSoda.isChecked():
            amount = amount + 3
        if self.ui.checkBoxTea.isChecked():
            amount = amount + 1

        self.ui.labelAmount.setText(f"Total amount is: R{amount}")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyForm()
    window.show()

    sys.exit(app.exec_())