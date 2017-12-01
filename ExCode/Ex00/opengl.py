from OpenGL.GL import *
from OpenGL.GLUT import *

global angle
angle = 0

def draw():
    global angle
    angle += 0.1;
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotate(angle, 1,1,0)
    glutWireTeapot(0.5)
    glFlush()

glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250, 250)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"OpenGL with Python")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()