from PyQt5.QtWidgets import *
from opengl_widget import *
from start_screen import *

class main_window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.StartScreen=StartSc()
        self.setCentralWidget(self.StartScreen)
        self.setWindowTitle("pyqt_game")
        self.setGeometry(300,300,800,600)
        self.setFixedSize(800,600)
        self.StartScreen.destroyed.connect(self.gl_init)

    def gl_init(self):
        self.gl_Widget = OpenGL_Widget(self)
        self.gl_Widget.update()
        self.setCentralWidget(self.gl_Widget)
        self.gl_Widget.show()

        self.gl_Widget.timer.timeout.connect(self.gl_Widget.Loop)
        self.gl_Widget.timer.start(1000 / 60)