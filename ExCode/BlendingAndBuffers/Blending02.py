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
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA );
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)



def myDisp ():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(-1, 1.0, 5, 0, 0, 0, 0, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0,0,1,0])

    glColor4f(1,1,0,1.0)
    glutSolidTeapot(0.5)


    glTranslatef(0,0,1)
    glColor4f(0,0,1,0.5)
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
    glutSolidTeapot(0.5)
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glDepthFunc(GL_EQUAL)
    glutSolidTeapot(0.5)
    glDepthFunc(GL_LESS)

    glTranslatef(0, 0, 1)
    glColor4f(1, 0, 1, 0.5)
    glColorMask(GL_FALSE, GL_FALSE, GL_FALSE, GL_FALSE)
    glutSolidTeapot(0.5)
    glColorMask(GL_TRUE, GL_TRUE, GL_TRUE, GL_TRUE)
    glDepthFunc(GL_EQUAL)
    glutSolidTeapot(0.5)
    glDepthFunc(GL_LESS)

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGBA)
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