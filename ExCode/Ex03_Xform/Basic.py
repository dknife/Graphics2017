from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import myDraw as md


angle = 0.0

def disp() :

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1.0, 0.1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(1,2,6, 0,0,0, 0,1,0)


    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT)

    # draw objects
    md.drawAxes()


    # body
    md.box(0.1, 2.0, 0.1, 1,0,0)

    glPushMatrix();

    global angle
    angle += 0.1

    # arm 1
    glTranslatef(0,1,0)
    glRotatef(45, 0,0,1)
    glRotatef(angle, 0, 1, 0)
    glTranslatef(0,1,0)

    md.box(0.1, 2.0, 0.1, 1, 1, 0)

    glPopMatrix()

    # arm 2
    glTranslatef(0, 1, 0)
    glRotatef(-45, 0, 0, 1)
    glRotatef(angle, 0, 1, 0)
    glTranslatef(0, 1, 0)

    md.box(0.1, 2.0, 0.1, 1, 1, 0)


    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

md.myGLInit()


# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)

# enter main infinite-loop
glutMainLoop()




