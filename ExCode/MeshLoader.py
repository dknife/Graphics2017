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

# initialization
def GLinit() :

    glClearColor(0,0,1,0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, Ld)
    glLightfv(GL_LIGHT0, GL_SPECULAR, Ls)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, Md)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Ms)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)



def loadMesh(filename):
    print(filename)
    with open(filename, "rt") as mesh :
        nV = int(next(mesh))
        verts = [[0,0,0] for idx in range(nV)]
        for i in range(0, nV) :
            verts[i][0], verts[i][1], verts[i][2] = [float(x) for x in next(mesh).split()]
        nF = int(next(mesh))
        faces = [[0,0,0] for idx in range(nF)]
        for i in range(0, nF) :
            faces[i][0], faces[i][1], faces[i][2] = [int(x) for x in next(mesh).split()]
    return verts, faces


V, F = loadMesh("testMesh.txt")
print(V)
print(F)


def computeNormal(p1, p2, p3) :
    u = np.array([p2[i] - p1[i] for i in range(0, 3)])
    v = np.array([p3[i] - p1[i] for i in range(0, 3)])
    N = np.cross(u,v)
    l = np.linalg.norm(N)
    if l > 0.01 :
        N = N / l
    else :
        N = [0,1,0]
    return N

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



    # draw vertices
    nV = len(V)
    nF = len(F)

    glRotatef(t*10, 0,1,0)


    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)

    for i in range(nF) :
        p1, p2, p3 = F[i][0], F[i][1], F[i][2]
        N = computeNormal(V[p1], V[p2], V[p3])
        glNormal3fv(N)
        glVertex3fv(V[p1])
        glVertex3fv(V[p2])
        glVertex3fv(V[p3])

    glEnd()


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