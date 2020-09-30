from OpenGL.GL import *
from OpenGL.GL.shaders import *

class Shader:
    def __init__(self,file):
        vs=self.Create_shader(self.Read_shader(file+'.vs'),GL_VERTEX_SHADER)
        fs=self.Create_shader(self.Read_shader(file+'.fs'),GL_FRAGMENT_SHADER)
        self.program=glCreateProgram()
        glAttachShader(self.program,vs)
        glAttachShader(self.program,fs)
        glLinkProgram(self.program)
        result = glGetProgramiv(self.program, GL_LINK_STATUS)
        if not (result):
            raise RuntimeError(glGetProgramInfoLog(self.program))

    def Read_shader(self,filename):
        with open(filename,'r') as f:
            mas=f.read().splitlines()
        text=''
        for i in range(len(mas)):
            text+=mas[i]+'\n'

        return text

    def Create_shader(self, text, type):
        Shader=glCreateShader(type)
        glShaderSource(Shader, text)
        glCompileShader(Shader)
        result = glGetShaderiv(Shader, GL_COMPILE_STATUS)
        if not (result):
            print(glGetShaderInfoLog(Shader))
        return Shader

    def GetShader(self):
        return self.program