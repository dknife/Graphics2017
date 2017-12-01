from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math


def drawCubes() :

    for i in range(-20,20) :
        for j in range(-20, 20):
            glPushMatrix()
            glTranslatef(i,0,j)
            glutSolidSphere(0.4, 20,20)
            glPopMatrix()



angle = 0
def disp() :
    global angle


    glAccum(GL_LOAD, 0.0)

    angle += 0.1
    glRotatef(angle, 0,1,0)
    for camx in range(-5,5) :
        for camy in range(-5,5) :

            # reset buffer
            #----------------------------------------
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(50, 1.0, 0.1, 1000)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            gluLookAt(camx*0.1,camy*0.1+10,30, 0,0,0, 0,1,0)

            # drawing
            glColor3f(1,1,0)
            drawCubes()

            #-----------------------------------------
            glAccum(GL_ACCUM, 1.0/(121.0))

    # glAccum(op, value)
    # op: GL_MULT, GL_ACCUM, GL_RETURN, GL_LOAD, GL_ADD
    #
    glAccum(GL_RETURN, 1.0)

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_ACCUM | GLUT_DEPTH |GLUT_RGB)

glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

glClearColor(0, 0.0, 0.0, 0)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_COLOR_MATERIAL)

# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)

# enter main infinite-loop
glutMainLoop()
