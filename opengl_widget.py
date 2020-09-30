from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget
from mesh import *
from Shader import *
import time

class OpenGL_Widget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGL_Widget,self).__init__(parent)
        self.setGeometry(300,300,800,600)
        self.vert=[-0.5,-0.5,0.0,0.0,0.0,
                   0.5,0.5,0.0,0.0,0.0,
                   0.5,-0.5,0.0,0.0,0.0,
                   -0.5,-0.5,0.0,0.0,0.0,
                   -0.5,0.5,0.0,0.0,0.0,
                   0.5,0.5,0.0,0.0,0.0]
        self.shade_file='basic'
        self.Mesh=0
        self.hide()

    def initializeGL(self):
        glClearColor(0.3,0.5,0.5,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        self.setOpenGL()


    def paintGL(self):
        self.Mesh.DrawMesh(self.shader.GetShader())

    def SetShader(self,file):
        self.shader=Shader(file)

    def SetMesh(self,vert):
        self.Mesh=mesh(vert)
        self.Mesh.InitMesh(self.shader.GetShader())

    def setOpenGL(self):
        self.SetShader(self.shade_file)
        self.SetMesh(self.vert)

    def SetShader_file(self,file):
        self.shade_file=file

    def Set_Vertex(self,vert):
        for i in range(len(vert)):
            self.vert[i]=vert[i]