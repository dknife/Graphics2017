from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np
import math


def GLinit() :
    glClearColor(1, 1, 1, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);

def drawQuad(x,y,z) :
    glPushMatrix()
    glTranslatef(x,y,z)
    glBegin(GL_QUADS)
    glVertex3f(-1, 1, 0)
    glVertex3f(-1,-1, 0)
    glVertex3f( 1,-1, 0)
    glVertex3f( 1, 1, 0)
    glEnd()
    glPopMatrix()

angle = 0

def myDisp ():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0,2,5, 0,0,0, 0,1,0)

    glRotatef(angle, 0,1,0)
    angle += 0.05
    glColor4f(1,1,0,0.5)
    drawQuad(0,0,0)
    glColor4f(0, 1, 1, 0.5)
    drawQuad(0,0,-1)

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