from OpenGL.GL import *
from PyQt5.QtGui import *
import math
import matrix

class camera:
    def __init__(self,width,height):
        self.CameraPos=matrix.vector3f(0.0,0.0,0.0)
        self.CameraDir=matrix.vector3f(0.0,0.0,-1.0)
        self.CameraUp=matrix.vector3f(0.0,1.0,0.0)
        self.ViewMatrix=matrix.mat4()
        self.PerspectiveMatrix=matrix.mat4()
        self.Set_View_Matrix()
        self.Set_Perspective_Matrix(width,height)

    def Set_View_Matrix(self):
        self.ViewMatrix=matrix.LookAt(self.CameraPos,self.CameraDir,self.CameraUp)

    def Set_Perspective_Matrix(self,width,height):
        self.PerspectiveMatrix=matrix.Projection(90.0,float(width)/float(height),0.1,100.0)

    def MoveCamera(self,vec):
        self.CameraPos+=vec

    def Get_View(self):
        return matrix.To_np(self.ViewMatrix)

    def Get_Projection(self):
        return matrix.To_np(self.PerspectiveMatrix)