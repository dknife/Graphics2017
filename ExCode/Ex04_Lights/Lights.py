from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

L_diffuse = [1.0, 0.0, 0.0, 1.0]
L_position = [5.0, 5.0, 0.0, 1.0]
M_diffuse = [1.0, 1.0, 1.0, 1.0]

def SetLighting() :
    global L_diffuse, M_diffuse
    glMaterialfv(GL_FRONT, GL_DIFFUSE, M_diffuse)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, L_diffuse)

def SetLightPosition() :
    global L_position
    glLightfv(GL_LIGHT0, GL_POSITION, L_position)

def disp() :
    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1.0, 0.1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    SetLightPosition()

    glutSolidTeapot(1.0)
    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_DEPTH|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_DEPTH_TEST)
SetLighting()
glClearColor(0, 0.0, 0.0, 0)


# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)

# enter main infinite-loop
glutMainLoop()