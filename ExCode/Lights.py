from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import random as rnd

nLight = 8

Ld = [[1,1,1,1] for x in range(0,nLight)]
Ls = [[1,1,1,1] for x in range(0,nLight)]
Lp = [[1,1,1,1] for x in range(0,nLight)]

Md = [1,1,1,1]
Ms = [1,1,1,1]
shininess = [127.0]

t = 0

def LightSet():
    for i in range(0, nLight) :
        Ld[i] = [rnd.randrange(0,701)/1000.0+0.3,
                 rnd.randrange(0,701)/1000.0+0.3,
                 rnd.randrange(0,701)/1000.0+0.3, 1]
        glLightfv(GL_LIGHT0+i, GL_DIFFUSE, Ld[i])
        glLightfv(GL_LIGHT0+i, GL_SPECULAR, Ls[i])
        #spot light setting
        glLightf (GL_LIGHT0+i, GL_SPOT_CUTOFF, i*2+30.0)
        glLightfv(GL_LIGHT0+i, GL_SPOT_DIRECTION, [0,0,-1])
        glLightf (GL_LIGHT0+i, GL_SPOT_EXPONENT, 10.0)
        #

    glMaterialfv(GL_FRONT, GL_DIFFUSE, Md)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Ms)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

def LightPosition(t):
    for i in range(0, nLight) :
        w = float(i+1)
        if i%2 is 0 :
            t = -t/2.0
        Lp[i][0] = 5.0*math.sin(w*t)
        Lp[i][1] = 5.0*math.cos(w*t)
        Lp[i][2] = 5.0
        glLightfv(GL_LIGHT0+i, GL_POSITION, Lp[i])

def glInit() :
    glClearColor(0,1,0,1)
    glEnable(GL_LIGHTING)
    for i in range(0, nLight) :
        glEnable(GL_LIGHT0 + i)
    glEnable(GL_DEPTH_TEST)
    LightSet()


def disp() :
    global t
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # CAMERA
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluPerspective(60, 1.0, 0.1, 1000)
    glOrtho(-6,6,-6,6, -100,100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10, 0,0,0, 0,1,0)

    t+= 0.01
    LightPosition(t)
    # OBJECTS
    for x in range(-5, 6) :
        for y in range(-5, 6) :
            glPushMatrix()
            glTranslatef(x, y, 0)
            glutSolidSphere(0.5, 20,20)
            glPopMatrix()

    glFlush()

# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(50,50)
glutCreateWindow(b'Hello Lights')

# initialization
glInit()

# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)


# enter main loop
glutMainLoop()
