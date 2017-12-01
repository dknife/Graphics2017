from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def myGLInit() :
    glLineWidth(4)
    glClearColor(0, 0.5, 0.5, 0)


def drawMyCircle(time, zVal) :

    # a Circle
    angle = 0.0
    angleStep = 2.0 * 3.141592 / 100.0

    glBegin(GL_LINE_LOOP)
    for i in range(0, 100):
        angle += angleStep
        glVertex3f(math.cos(angle), math.sin(angle), zVal)
    glEnd()

    # a Rotating Line
    glBegin(GL_LINES)
    glColor(1, 1, 0)
    glVertex3f(0, 0, zVal)
    glColor(0, 1, 0)

    glVertex3f(math.cos(time), math.sin(time), zVal)
    glEnd()
