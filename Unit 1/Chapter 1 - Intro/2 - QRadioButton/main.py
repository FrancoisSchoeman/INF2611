#* Radio buttons
# Radio buttons are popular when the user needs to make a single selection from a list of items.
# They are used in groups, and only one radio button in a group can be selected at a time.
# Radio buttons are created using the QRadioButton class.

#* QRadioButton methods
# setText() - sets the text of label of a radio button.
# isChecked() - returns True if a radio button is checked.
# setChecked() - used to check a radio button.
# setIcon() -s used to set an icon on a radio button.

#* QRadioButton signals
# toggled - is emitted when the radio button is toggled.
# clicked - is emitted when the radio button is clicked.
# stateChanged - is emitted when the state of the radio button changes.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.radioButtonFirstClass.toggled.connect(self.dispFare)
        self.ui.radioButtonBusinessClass.toggled.connect(self.dispFare)
        self.ui.radioButtonEconomyClass.toggled.connect(self.dispFare)

        self.show()

    def dispFare(self):
        fare = 0
        if self.ui.radioButtonFirstClass.isChecked():
            fare = 150
        if self.ui.radioButtonBusinessClass.isChecked():
            fare = 125
        if self.ui.radioButtonEconomyClass.isChecked():
            fare = 100

        self.ui.labelFare.setText(f"Air Fare is {fare}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = MyForm()
    w.show()

    sys.exit(app.exec_())
        
