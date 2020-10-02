import math
import numpy as np

class vector3f:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.mas=[x,y,z]

class mat4:
    def __init__(self):
        self.mas=[1.0,0.0,0.0,0.0,
                  0.0,1.0,0.0,0.0,
                  0.0,0.0,1.0,0.0,
                  0.0,0.0,0.0,1.0]
    def Set(self,mas):
        for i in range(16):
            self.mas[i]=mas[i]

def Projection(fov,aspect,zNear,zFar):
    out=mat4()
    f=1/math.tan(math.radians(fov/2.0))
    out.Set([f / aspect, 0.0, 0.0, 0.0,
             0.0, f, 0.0, 0.0,
             0.0, 0.0, (zFar + zNear) / (zNear-zFar), (-2 * zFar * zNear) / (zFar - zNear),
             0.0, 0.0, -1.0, 0.0])
    return Transplon(out)

def normalize(vec):
    out=vector3f()
    out.mas[0]=vec.mas[0]/math.sqrt(vec.mas[0]*vec.mas[0]+vec.mas[1]*vec.mas[1]+vec.mas[2]*vec.mas[2])
    out.mas[1]=vec.mas[1]/math.sqrt(vec.mas[0]*vec.mas[0]+vec.mas[1]*vec.mas[1]+vec.mas[2]*vec.mas[2])
    out.mas[2]=vec.mas[2]/math.sqrt(vec.mas[0]*vec.mas[0]+vec.mas[1]*vec.mas[1]+vec.mas[2]*vec.mas[2])
    return out


def dot(vec,vec1):
    return vec.mas[0]*vec1.mas[0]+vec.mas[1]*vec1.mas[1]+vec.mas[2]*vec1.mas[2]

def vector_sum(vec,vec1):
    out=vector3f()
    out.mas[0]=vec.mas[0]+vec1.mas[0]
    out.mas[1]=vec.mas[1]+vec1.mas[1]
    out.mas[2]+vec.mas[2]+vec1.mas[2]
    return out

def mul_vector_on_scalar(vec,scalar):
    out=vector3f()
    out.mas[0]=vec.mas[0]*scalar
    out.mas[1]=vec.mas[1]*scalar
    out.mas[2]=vec.mas[2]*scalar
    return out

def cross(vec,vec1):
    i=vector3f()
    j=vector3f()
    k=vector3f()

    i.mas[0]=1
    i.mas[1]=0
    i.mas[2]=0

    j.mas[0]=0
    j.mas[1]=1
    j.mas[2]=0

    k.mas[0]=0
    k.mas[1]=0
    k.mas[2]=1

    a=mul_vector_on_scalar(i,(vec.mas[1]*vec1.mas[2]-vec.mas[2]*vec1.mas[1]))
    b=mul_vector_on_scalar(j,(vec.mas[0]*vec1.mas[2]-vec.mas[2]*vec1.mas[0]))
    b=mul_vector_on_scalar(b,-1)
    c=mul_vector_on_scalar(k,(vec.mas[0]*vec1.mas[1]-vec.mas[1]*vec1.mas[0]))
    return vector_sum(a,vector_sum(b,c))

def LookAt(CameraPos,CameraFront,CameraUp):
    zaxis=normalize(CameraFront)
    xaxis=normalize(cross(CameraUp,zaxis))
    yaxis=cross(zaxis,xaxis)

    out=mat4()

    out.mas=[xaxis.mas[0],yaxis.mas[0],zaxis.mas[0],0.0,
             xaxis.mas[1],yaxis.mas[1],zaxis.mas[1],0.0,
             xaxis.mas[2],yaxis.mas[2],zaxis.mas[2],0.0,
             -CameraPos.mas[0],-CameraPos.mas[1],-CameraPos.mas[2],1.0]
    return out

def Rotate(angle,vec):
    out=mat4()
    if vec.mas[0]==1:
        out.mas[0] = 1
        out.mas[4] = 0
        out.mas[8] = 0
        out.mas[12] = 0

        out.mas[1] = 0
        out.mas[5] = math.cos(math.radians(angle))
        out.mas[9] = math.sin(math.radians(angle))
        out.mas[13] = 0

        out.mas[2] = 0
        out.mas[6] = -math.sin(math.radians(angle))
        out.mas[10] = math.cos(math.radians(angle))
        out.mas[14] = 0

        out.mas[3] = 0
        out.mas[7] = 0
        out.mas[11] = 0
        out.mas[15] = 1

    elif vec.mas[1]==1:
        out.mas[0] = math.cos(math.radians(angle))
        out.mas[4] = 0
        out.mas[8] = math.sin(math.radians(angle))
        out.mas[12] = 0

        out.mas[1] = 0
        out.mas[5] = 1
        out.mas[9] = 0
        out.mas[13] = 0

        out.mas[2] = -math.sin(math.radians(angle))
        out.mas[6] = 0
        out.mas[10] = math.cos(math.radians(angle))
        out.mas[14] = 0

        out.mas[3] = 0
        out.mas[7] = 0
        out.mas[11] = 0
        out.mas[15] = 1

    elif vec.mas[2]==1:
        out.mas[0] = math.cos(math.radians(angle))
        out.mas[4] = -math.sin(math.radians(angle))
        out.mas[8] = 0
        out.mas[12] = 0

        out.mas[1] = math.sin(math.radians(angle))
        out.mas[5] = math.cos(math.radians(angle))
        out.mas[9] = 0
        out.mas[13] = 0

        out.mas[2] = 0
        out.mas[6] = 0
        out.mas[10] = 1
        out.mas[14] = 0

        out.mas[3] = 0
        out.mas[7] = 0
        out.mas[11] = 0
        out.mas[15] = 1

    return Transplon(out)

def Transplon(mat):
    out=mat4()
    out.mas[0]=mat.mas[0]
    out.mas[1]=mat.mas[4]
    out.mas[2]=mat.mas[8]
    out.mas[3]=mat.mas[12]

    out.mas[4] = mat.mas[1]
    out.mas[5] = mat.mas[5]
    out.mas[6] = mat.mas[9]
    out.mas[7] = mat.mas[13]

    out.mas[8] = mat.mas[2]
    out.mas[9] = mat.mas[6]
    out.mas[10] = mat.mas[10]
    out.mas[11] = mat.mas[14]

    out.mas[12] = mat.mas[3]
    out.mas[13] = mat.mas[7]
    out.mas[14] = mat.mas[11]
    out.mas[15] = mat.mas[15]

    return out

def To_np(mas):
    return np.array(mas.mas,np.float32)