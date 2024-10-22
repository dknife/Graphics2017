from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math


angle = 0.0

def drawPlanet(distance, angle, planetRadius) :

    glBegin(GL_LINE_STRIP)
    for i in range(0, 360):
        theta = 2.0 * 3.141592 * i / 360.0
        x = distance * math.cos(theta)
        y = distance * math.sin(theta)
        glVertex3f(x, 0, y)
    glEnd()

    glRotatef(angle, 0, 1, 0)
    glTranslatef(distance, 0, 0)

    glutWireSphere(planetRadius, 20, 20)


def disp() :
    global angle

    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1.0, 0.1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10,30,40, 0,0,0, 0,1,0)

    # drawing

    # sun
    glColor3f(1,0,0)
    glutWireSphere(1.0, 20, 20)

    angle += 0.2

    glPushMatrix()
    # mercury
    glColor(0.5,0.5,0.5)
    drawPlanet(3, 3.0*angle, 0.3)
    glPopMatrix()


    glPushMatrix()
    # earth
    glColor3f(0,0.5,1.0)
    glRotatef(5, 1, 0, 0)
    drawPlanet(10.0, angle, 0.5)

    # moon
    glColor3f(1.0,1.0, 1.0)
    glRotatef(-5, 1, 0, 0)
    drawPlanet(1.0, angle*10.0, 0.2)
    glPopMatrix()

    glPushMatrix()
    # jupiter
    glColor3f(1.0, 0.3, 0.2)
    glRotatef(-5, 1, 0, 0)
    drawPlanet(15, angle*0.5, 1.5)

    glPushMatrix()
    # jupiter's moon 1
    glColor3f(0.0, 1.0, 1.0)
    glRotatef(15, 1, 0, 0)
    drawPlanet(2.0, angle * 5.0, 0.2)
    glPopMatrix()

    # jupiter's moon 2
    glColor3f(1.0, 1.0, 0.0)
    glRotatef(-15, 1, 0, 0)
    drawPlanet(3.0, angle * 7.0, 0.2)
    glPopMatrix()

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

glClearColor(0, 0.0, 0.0, 0)


# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)

# enter main infinite-loop
glutMainLoop()