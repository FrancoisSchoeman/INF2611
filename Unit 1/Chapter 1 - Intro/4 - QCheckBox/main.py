# Diplaying options in the form of checkboxes

#* QCheckBoxes allow the user to select multiple options from a list of options.

#* Methods
# setCheckState() - sets the state of the checkbox
# checkState() - returns the state of the checkbox
# toggle() - toggles the state of the checkbox
# isChecked() - returns True if the checkbox is checked, else False
# setTristate() - if set to True, the user will not be able to check or uncheck the checkbox.
# isTristate() - returns True if the checkbox is tristate, else False
# setAutoExclusive() - sets the autoexclusive of the checkbox
# isAutoExclusive() - returns True if the checkbox is autoexclusive, else False
# setCheckable() - sets the checkable of the checkbox
# isCheckable() - returns True if the checkbox is checkable, else False
# setIcon() - sets the icon of the checkbox
# icon() - returns the icon of the checkbox
# setIconSize() - sets the icon size of the checkbox
# iconSize() - returns the icon size of the checkbox
# setText() - sets the text of the checkbox
# text() - returns the text of the checkbox

#* Signals
# stateChanged - is emitted when the state of the checkbox is changed
# toggled - is emitted when the checkbox is toggled
# clicked - is emitted when the checkbox is clicked
# pressed - is emitted when the checkbox is pressed
# released - is emitted when the checkbox is released
# entered - is emitted when the mouse enters the checkbox
# exited - is emitted when the mouse exits the checkbox

import sys
from PyQt5.QtWidgets import QDialog, QApplication

from ui import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlives.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausages.stateChanged.connect(self.dispAmount)

        self.show()


    def dispAmount(self):
        amount = 10

        if self.ui.checkBoxCheese.isChecked():
            amount += 1
        if self.ui.checkBoxOlives.isChecked():
            amount += 1
        if self.ui.checkBoxSausages.isChecked():
            amount += 2

        self.ui.labelAmount.setText(f"Total amount due: R{amount}")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyForm()
    window.show()

    sys.exit(app.exec_())
