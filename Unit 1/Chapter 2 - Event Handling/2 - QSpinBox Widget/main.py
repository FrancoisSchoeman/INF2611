# The Spin Box widget is used for displaying integer values, floating-point values, and text.
# It applies a constraint on the user: the user cannot enter any random data, but can select
# only from the available options displayed through Spin Box. A Spin Box widget displays
# an initial value by default that can be increased or decreased by selecting the up/down
# button or up/down arrow key on the keyboard. You can choose a value that is displayed by
# either clicking on it or typing it in manually

# A Spin Box widget can be created using two classes, QSpinBox and QDoubleSpinBox,
# where QSpinBox displays only integer values, and the QDoubleSpinBox class displays
# floating-point values.

#* QSpinBox Methods:
#* value(): This method returns the current integer value selected from the spin box.
#* text(): This method returns the text displayed by the spin box.
#* setPrefix(): This method assigns the prefix text that is prepended to the value returned by the spin box.
#* setSuffix(): This method assigns the suffix text that is to be appended to the value returned by the spin box.
#* cleanText(): This method returns the value of the spin box without a suffix, a 
# prefix, or leading or trailing whitespaces.
#* setValue(): This method assigns the value to the spin box.
#* setSingleStep(): This method sets the step size of the spin box.
#* setMinimum(): This method sets the minimum value of the spin box.
#* setMaximum(): This method sets the maximum value of the spin box.
#* setWrapping(): Enable looping of the min and max values

#* QSpinBox Signals
#* valueChanged(): Emitted when the value of the spin box is changed
#* editingFinished(): Emitted when focus is lost on the spin box

# The defaults are minimum = 0, maximum = 99, singleStep = 1, value = 0,
# and of a double spin box are minimum = 0.000000, maximum = 99990000, singleStep = 1, value = 0.000000.

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ui import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.spinBoxBookQty.editingFinished.connect(self.result1)
        self.ui.doubleSpinBoxSugarWeight.editingFinished.connect(self.result2)

        self.show()

    def result1(self):
        if len(self.ui.lineEditBookPrice.text()) != 0:
            bookPrice = int(self.ui.lineEditBookPrice.text())
        else:
            bookPrice = 0

        totalBookAmount = self.ui.spinBoxBookQty.value() * bookPrice
        
        self.ui.lineEditBookAmount.setText(str(totalBookAmount))
        
        
    def result2(self):
        if len(self.ui.lineEditSugarPrice.text()) != 0:
            sugarPrice = float(self.ui.lineEditSugarPrice.text())
        else:
            sugarPrice = 0

        totalSugarAmount = self.ui.doubleSpinBoxSugarWeight.value() * sugarPrice

        self.ui.lineEditSugarAmount.setText(str(round(totalSugarAmount,2)))

        totalBookAmount = int(self.ui.lineEditBookAmount.text())
        totalAmount = totalBookAmount + totalSugarAmount

        self.ui.labelTotalAmount.setText(str(round(totalAmount,2)))



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyForm()
    window.show()

    sys.exit(app.exec_())