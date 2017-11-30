from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np
import math


def GLinit() :
    glClearColor(0, 1, 1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_STENCIL_TEST);



def myDisp ():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(-1, 1.0, 5, 0, 0, 0, 0, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0,0,1,0])

    glClear(GL_STENCIL_BUFFER_BIT)
    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
    glDepthMask(GL_FALSE)
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(0.0, -1.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glEnd()
    glStencilFunc(GL_EQUAL, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glDepthMask(GL_TRUE)
    glColor3f(1, 1, 0)
    glutSolidTeapot(0.7)

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_STENCIL | GLUT_RGBA)
glutInitWindowPosition(0,0)
glutInitWindowSize(512,512)
glutCreateWindow(b'Blending')

# initialization
GLinit()


# callback registration
glutDisplayFunc(myDisp)
glutIdleFunc(myDisp)


# enter main loop
glutMainLoop()