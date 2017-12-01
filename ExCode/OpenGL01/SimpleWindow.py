from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

def myDisp() :
    glClearColor(0.5,0.5,0.5,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(100,100)
glutCreateWindow(b"my first opengl window")

glutDisplayFunc(myDisp)
glutMainLoop()
