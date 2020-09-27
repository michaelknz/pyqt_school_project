from main_window import *
from PyQt5 import QtWidgets


app = QtWidgets.QApplication([])
win = main_window()
win.show()
app.exec_()