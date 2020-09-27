from PyQt5 import uic
from PyQt5.QtWidgets import QWidget,QPushButton

class StartSc(QWidget):
    def __init__(self, parent=None):
        super(StartSc,self).__init__(parent)
        uic.loadUi('start_screen.ui',self)
        btn=self.findChild(QPushButton,'start')
        btn.clicked.connect(self.on_stclick)

    def on_stclick(self):
        self.deleteLater()