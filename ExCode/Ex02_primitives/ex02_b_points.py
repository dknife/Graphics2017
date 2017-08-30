from OpenGL.GLUT import *
from OpenGL.GL import *

x = -1.0

def draw() :
    global x
    glClear(GL_COLOR_BUFFER_BIT)

    glPointSize(5)
    glBegin(GL_POINTS)
    y = x * x
    glColor3f(1.0, y, 1.0)
    glVertex3f(x, y, 0)
    x += 0.0001
    if x > 1.0 :
        x = x - 2.0
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