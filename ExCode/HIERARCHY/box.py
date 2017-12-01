from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math


angle = 0.0

def drawRect(r,g,b) :

    glColor3f(r,g,b)
    glBegin(GL_QUADS)
    glVertex2f(-1, 1)
    glVertex2f(-1,-1)
    glVertex2f( 1,-1)
    glVertex2f( 1, 1)
    glEnd()



def disp() :
    global angle
    angle += 0.001

    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1.0, 0.1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(4.0*math.cos(angle),4,4.0*math.sin(angle), 0,0,0, 0,1,0)

    # drawing
    glColor3f(1,1,0)


    glPushMatrix()
    glTranslatef(0,0,1)
    drawRect(1,0,0)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,-1)
    drawRect(0,1,0)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 0,1,0)
    glTranslatef(0, 0, 1)
    drawRect(0,0,1)
    glTranslatef(0, 0, -2)
    drawRect(1,1,0)
    glPopMatrix()

    glPushMatrix()
    glRotatef(90, 1,0,0)
    glTranslatef(0, 0, 1)
    drawRect(0,1,1)
    glTranslatef(0, 0, -2)
    drawRect(1,0,1)
    glPopMatrix()

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_DEPTH|GLUT_RGB)

glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

## INIT
glClearColor(0, 0.0, 0.0, 0)
glEnable(GL_DEPTH_TEST)

# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)

# enter main infinite-loop
glutMainLoop()

