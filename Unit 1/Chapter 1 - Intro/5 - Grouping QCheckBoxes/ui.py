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
        Dialog.resize(529, 444)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 201, 16))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(240, 30, 251, 20))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(230, 60, 261, 71))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.checkBoxChoclateChips = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxChoclateChips.setGeometry(QtCore.QRect(20, 10, 231, 20))
        self.checkBoxChoclateChips.setObjectName("checkBoxChoclateChips")
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.groupBox)
        self.checkBoxCookieDough.setGeometry(QtCore.QRect(20, 40, 231, 20))
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setEnabled(True)
        self.checkBox_4.setGeometry(QtCore.QRect(240, 240, 251, 20))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(230, 270, 261, 101))
        self.groupBoxDrinks.setTitle("")
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxCoffee.setGeometry(QtCore.QRect(20, 10, 231, 20))
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxSoda.setGeometry(QtCore.QRect(20, 40, 231, 20))
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxTea.setGeometry(QtCore.QRect(20, 70, 231, 20))
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 201, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(230, 140, 261, 71))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBoxChoclateAlmond = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxChoclateAlmond.setGeometry(QtCore.QRect(20, 10, 231, 20))
        self.checkBoxChoclateAlmond.setObjectName("checkBoxChoclateAlmond")
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBoxRockyRoad.setGeometry(QtCore.QRect(20, 40, 231, 20))
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(20, 379, 471, 51))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Select Your Ice Cream"))
        self.checkBox.setText(_translate("Dialog", "Ice Creams"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Chocolate Chips R4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough R2"))
        self.checkBox_4.setText(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee R2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda R3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea R1"))
        self.label_2.setText(_translate("Dialog", "Select Your Drink"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Chocolate Almond R3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road R5"))
