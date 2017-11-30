from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np
import math


def GLinit() :
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_STENCIL_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)



angle = 0
def myDisp ():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(-1, 3.0, 5, 0, 0, 0, 0, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, [0,0,1,0])

    angle += 0.1

    glClear(GL_STENCIL_BUFFER_BIT)
    # 주전자  그리기

    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glColor3f(0.0, 0.5, 1.0)
    glPushMatrix()
    glTranslated(0.0, 1.0, 0.0)
    glRotated(angle, 0.0, 0.0, 1.0)
    glutSolidTeapot(0.7)
    glPopMatrix()

    # 거울을 위한 스텐실 영역 설정
    glColorMask(0, 0, 0, 0)
    glDepthMask(0)
    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.0, 0.0, 2.0)
    glVertex3f(2.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glColorMask(1, 1, 1, 1)
    glDepthMask(1)

    glStencilFunc(GL_EQUAL, 0x1, 0x1)
    # 주전자의 거울상 그리기
    glColor3f(0.0, 0.5, 1.0)
    glPushMatrix()
    glScalef(1.0, -1.0, 1.0)
    glTranslated(0.0, 1.0, 0.0)
    glRotated(angle, 0.0, 0.0, 1.0)
    glutSolidTeapot(0.7)
    glPopMatrix()


    # 거울 그리기
    glColor4f(1.0, 1.0, 1.0, 0.5);
    glBegin(GL_TRIANGLES);
    glVertex3f(-2.0, 0.0, 2.0);
    glVertex3f(2.0, 0.0, 1.0);
    glVertex3f(0.0, 0.0, 0.0);
    glEnd();

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