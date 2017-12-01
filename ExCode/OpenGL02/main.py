from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import myDraw as md


t = 0.0


def disp() :

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(15, 1.0, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,2,5, 0,0,0, 0,1,0)


    global t
    t += 0.01
    # reset buffe
    glClear(GL_COLOR_BUFFER_BIT)

    # draw objects
    for i in range(0,10) :
        md.drawMyCircle(t, -i*0.5)
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




