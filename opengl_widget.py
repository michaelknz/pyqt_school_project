from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget

class OpenGL_Widget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGL_Widget,self).__init__(parent)
        self.setGeometry(300,300,800,600)
        self.hide()

    def initializeGL(self):
        glClearColor(0.3,0.5,0.5,1.0)
        glClear(GL_COLOR_BUFFER_BIT)


    def paintGL(self):
        glClearColor(0.3,0.5,0.5,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glColor3d(1.0,0.0,0.0)
        glVertex3d(-0.5,-0.5,0.0)
        glVertex3d(0.0,0.5,0.0)
        glVertex3d(0.5,-0.5,0.0)
        glEnd()