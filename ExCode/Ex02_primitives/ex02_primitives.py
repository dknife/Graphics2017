from OpenGL.GLUT import *
from OpenGL.GL import *


def draw() :
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-1.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 1.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(1.0, 0.0)
    glEnd()
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250, 250)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"OpenGL with Python")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()