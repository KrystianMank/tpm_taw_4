from PyQt5 import QtCore, QtGui, QtWidgets

def messagebox(title,message, icon, button):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        if icon == "Information":
            mess.setIcon(QtWidgets.QMessageBox.Icon.Information)
        elif icon == "Warning":
            mess.setIcon(QtWidgets.QMessageBox.Icon.Warning)

        if button == "Ok":
            mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        elif button =="Cancel":
            mess.setStandardButtons(QtWidgets.QMessageBox.Cancel)
        mess.exec_()