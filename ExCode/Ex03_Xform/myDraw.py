from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def myGLInit() :

    glClearColor(0, 0.5, 0.5, 0)


def box(dx, dy, dz, r,g,b) :
    glColor3f(r,g,b)
    glPushMatrix()
    glScalef(dx, dy, dz)
    glutWireCube(1.0)
    glPopMatrix()
    drawAxes()

def drawBoxWithAxes(r,g,b) :
    glColor3f(r,g,b)
    glutWireCube(1.0)
    drawAxes()

def drawTeapotWithAxes(r,g,b) :
    glColor3f(r,g,b)
    glutWireTeapot(0.25)
    drawAxes()


def drawAxes() :
    axisLength = 0.2
    glLineWidth(2)
    glBegin(GL_LINES)
    # x
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(axisLength,0,0)
    # y
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,axisLength,0)
    # z
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,axisLength)
    glEnd()
    glLineWidth(1)


