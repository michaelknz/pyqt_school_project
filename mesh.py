from OpenGL.GL import *
import numpy as np
import ctypes

class mesh:
    def __init__(self,mas):
        self.vao = 0
        self.vbo = 0
        self.vertices = []
        self.SetVertices(mas)

    def InitMesh(self,shader):
        self.vertices=np.array(self.vertices,dtype=np.float32)
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)

        glUseProgram(shader)

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, len(self.vertices)*4, self.vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, False, 5 * 4, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(1, 2, GL_FLOAT, False, 5 * 4, ctypes.c_void_p(3*4))
        glEnableVertexAttribArray(1)

        glBindVertexArray(0)

    def DrawMesh(self,shader):
        glClearColor(0.3, 0.5, 0.5, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glUseProgram(shader)

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES,0,len(self.vertices)//5)
        glBindVertexArray(0)

        glUseProgram(0)

    def SetVertices(self,mas):
        for i in range(len(mas)):
            self.vertices.append(mas[i])