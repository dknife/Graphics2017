from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np




# Light Properties
Ld = [1,1,1,1]
Ls = [1,1,1,1]
# Material Properties
Md = [1,1,0,1]
Ms = [1,1,1,1]
shininess = [120]


t = 0

# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np
import math

def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data




imgW1, imgH1, myImage1 = loadImage("sphere2.jpg")
tex = 0
nTexture = 1

def CreateTextures() :
    global tex, nTexture, imgW1, imgH1, myImage1

    tex = glGenTextures(nTexture)
    print(tex)

    glBindTexture(GL_TEXTURE_2D, tex)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imgW1, imgH1, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

    glEnable(GL_TEXTURE_2D)


# initialization
def GLinit() :

    glClearColor(0,0,0,0)
    CreateTextures()
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, Ld)
    glLightfv(GL_LIGHT0, GL_SPECULAR, Ls)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, Md)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Ms)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)


def computeNormal(p1, p2, p3) :
    u = np.array([p2[i] - p1[i] for i in range(0, 3)])
    v = np.array([p3[i] - p1[i] for i in range(0, 3)])
    N = np.cross(u,v)
    return N


def loadMesh(filename):
    print(filename)
    with open(filename, "rt") as mesh :
        nV = int(next(mesh))
        verts = [[0,0,0] for idx in range(nV)]
        normals = np.array([[0.0, 0.0, 0.0] for idx in range(nV)])
        for i in range(0, nV) :
            verts[i][0], verts[i][1], verts[i][2] = [float(x) for x in next(mesh).split()]
        nF = int(next(mesh))
        faces = [[0,0,0] for idx in range(nF)]
        for i in range(0, nF) :
            faces[i][0], faces[i][1], faces[i][2] = [int(x) for x in next(mesh).split()]
            Normal = computeNormal(verts[faces[i][0]],verts[faces[i][1]],verts[faces[i][2]])

            for points in range(3) :
                normals[faces[i][points]] = normals[faces[i][points]] + Normal


        for i in range(0, nV):
            len = np.linalg.norm(normals[i])
            if len > 0.000001 :
                normals[i] = normals[i]/len


    return verts, faces, normals


V1, F1, N1 = loadMesh("human.txt")
V2, F2, N2 = loadMesh("TestMesh.txt")



def drawMesh(v, n, f) :
    # draw vertices
    nV = len(v)
    nF = len(f)

    glBegin(GL_TRIANGLES)
    for i in range(nF):
        p1, p2, p3 = f[i][0], f[i][1], f[i][2]
        glNormal3fv(n[p1])
        glVertex3fv(v[p1])
        glNormal3fv(n[p2])
        glVertex3fv(v[p2])
        glNormal3fv(n[p3])
        glVertex3fv(v[p3])

    glEnd()


# display callback
def display() :
    global t, V, F

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # CAMERA SETTING
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,40,60, 0,40,0, 0,1,0)

    t += 0.1
    glLightfv(GL_LIGHT0, GL_POSITION, [math.sin(t),1,0,0])


    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)

    #glColor3f(1,0.8, 0.9)
    shininess = [5]
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)
    drawMesh(V1, N1, F1)
    #glColor3f(0,0,1)
    shininess = [127]
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)
    drawMesh(V2, N2, F2)

    glFlush()

# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH |GLUT_RGBA)
glutInitWindowSize(600,600)
glutInitWindowPosition(10,10)
glutCreateWindow(b"Light on Triangles")


GLinit()

# register callbacks
glutDisplayFunc(display)
glutIdleFunc(display)

# enter main-loop
glutMainLoop()