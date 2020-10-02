from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import QTimer
from mesh import *
from Shader import *
from camera import *

class OpenGL_Widget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(OpenGL_Widget,self).__init__(parent)
        self.setGeometry(300,300,800,600)
        self.Camera=camera(800,600)
        self.vert=[-0.5,-0.5,-1.0,0.0,0.0,
                   0.5,0.5,-1.0,0.0,0.0,
                   0.5,-0.5,-1.0,0.0,0.0,
                   -0.5,-0.5,-1.0,0.0,0.0,
                   -0.5,0.5,-1.0,0.0,0.0,
                   0.5,0.5,-1.0,0.0,0.0]
        self.shade_file='basic'
        self.Mesh=0
        self.angle=0
        self.hide()
        self.frameSwapped.connect(self.Start_timer)

    def initializeGL(self):
        glClearColor(0.3,0.5,0.5,1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        self.timer = QTimer()
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

    def Loop(self):
        self.context().currentContext().makeCurrent(self.context().currentContext().surface())
        self.angle+=0.01
        glUseProgram(self.shader.GetShader())
        glUniformMatrix4fv(glGetUniformLocation(self.shader.GetShader(), 'model'), 1, GL_FALSE, matrix.To_np(matrix.Rotate(self.angle,matrix.vector3f(0.0,0.0,1.0))))
        glUniformMatrix4fv(glGetUniformLocation(self.shader.GetShader(), 'view'), 1, GL_FALSE, self.Camera.Get_View())
        glUniformMatrix4fv(glGetUniformLocation(self.shader.GetShader(), 'projection'), 1, GL_FALSE, self.Camera.Get_Projection())
        glUseProgram(0)
        self.update()

    def Start_timer(self):
        self.timer.timeout.connect(self.Loop)
        self.timer.start(1000 / 30)