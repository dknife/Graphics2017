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


# display callback
def display() :
    global t

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # CAMERA SETTING
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,2,4, 0,0,0, 0,1,0)

    t += 0.01
    glLightfv(GL_LIGHT0, GL_POSITION, [math.sin(t),1,0,1])


    glBegin(GL_TRIANGLES)
    # triangle 1
    glColor3fv([1,0,0])
    p1 = np.array([ 0, 1, 0])
    p2 = np.array([ 0, 1, 1])
    p3 = np.array([ 1, 0, 0])
    u = p2 - p1 # vector from p1 to p2
    v = p3 - p1 # vector from p1 to p3
    normal = np.cross(u,v)
    normal = normal / (np.linalg.norm(normal))
    glNormal3fv(normal)
    glVertex3fv(p1)
    glVertex3fv(p2)
    glVertex3fv(p3)
    # triangle 2
    glColor3fv([0,1,1])
    p1 = np.array([ 0, 1, 0])
    p2 = np.array([-1, 0, 0])
    p3 = np.array([ 0, 1, 1])
    u = p2 - p1  # vector from p1 to p2
    v = p3 - p1  # vector from p1 to p3
    normal = np.cross(u, v)
    normal = normal / (np.linalg.norm(normal))
    glNormal3fv(normal)
    glVertex3fv(p1)
    glVertex3fv(p2)
    glVertex3fv(p3)
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