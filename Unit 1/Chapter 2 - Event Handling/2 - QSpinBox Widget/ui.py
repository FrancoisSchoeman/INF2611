# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 205)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 71, 16))
        self.label_2.setObjectName("label_2")
        self.labelTotalAmount = QtWidgets.QLabel(Dialog)
        self.labelTotalAmount.setGeometry(QtCore.QRect(280, 170, 111, 20))
        self.labelTotalAmount.setText("")
        self.labelTotalAmount.setObjectName("labelTotalAmount")
        self.lineEditBookPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookPrice.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEditBookPrice.setObjectName("lineEditBookPrice")
        self.lineEditSugarPrice = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarPrice.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.lineEditSugarPrice.setObjectName("lineEditSugarPrice")
        self.lineEditBookAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditBookAmount.setEnabled(False)
        self.lineEditBookAmount.setGeometry(QtCore.QRect(280, 60, 113, 20))
        self.lineEditBookAmount.setObjectName("lineEditBookAmount")
        self.lineEditSugarAmount = QtWidgets.QLineEdit(Dialog)
        self.lineEditSugarAmount.setEnabled(False)
        self.lineEditSugarAmount.setGeometry(QtCore.QRect(280, 120, 113, 20))
        self.lineEditSugarAmount.setObjectName("lineEditSugarAmount")
        self.spinBoxBookQty = QtWidgets.QSpinBox(Dialog)
        self.spinBoxBookQty.setGeometry(QtCore.QRect(220, 60, 42, 22))
        self.spinBoxBookQty.setObjectName("spinBoxBookQty")
        self.doubleSpinBoxSugarWeight = QtWidgets.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxSugarWeight.setGeometry(QtCore.QRect(210, 120, 62, 22))
        self.doubleSpinBoxSugarWeight.setObjectName("doubleSpinBoxSugarWeight")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Book Price"))
        self.label_2.setText(_translate("Dialog", "Sugar Price"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
