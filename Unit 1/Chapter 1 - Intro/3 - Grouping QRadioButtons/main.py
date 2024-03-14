#* Grouping Radio Buttons
# The QVBoxLayout class is used to create a vertical layout in code.
# We will use this to group the radio buttons together.

# You can also use the QButtonGroup class to group buttons together.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.radioButtonMedium.toggled.connect(self.dispSelected)
        self.ui.radioButtonLarge.toggled.connect(self.dispSelected)
        self.ui.radioButtonXL.toggled.connect(self.dispSelected)
        self.ui.radioButtonXXL.toggled.connect(self.dispSelected)

        self.ui.radioButtonDebitCard.toggled.connect(self.dispSelected)
        self.ui.radioButtonNetBanking.toggled.connect(self.dispSelected)
        self.ui.radioButtonCashOnDelivery.toggled.connect(self.dispSelected)

        self.show()


    def dispSelected(self):
        selected1 = ""
        selected2 = ""

        if self.ui.radioButtonMedium.isChecked():
            selected1 = "Medium"
        if self.ui.radioButtonLarge.isChecked():
            selected1 = "Large"
        if self.ui.radioButtonXL.isChecked():
            selected1 = "XL"
        if self.ui.radioButtonXXL.isChecked():
            selected1 = "XXL"

        if self.ui.radioButtonDebitCard.isChecked():
            selected2 = "Debit Card"
        if self.ui.radioButtonNetBanking.isChecked():
            selected2 = "Net Banking"
        if self.ui.radioButtonCashOnDelivery.isChecked():
            selected2 = "Cash On Delivery"

        self.ui.labelSelected.setText(f"Selected Shirt Size is {selected1} and\n Selected Payment Method is {selected2}")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyForm()
    window.show()

    sys.exit(app.exec_())