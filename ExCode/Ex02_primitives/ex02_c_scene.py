from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

import module_drawCircle as dc

def draw() :
    # camera lens
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    # lens modification
    glOrtho(-2, 2, -2, 2, -2, 2);

    # world
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();

    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_QUADS);
    glColor3f(1, 0, 0);
    glVertex3f(-0.5, 0.5, 0.0);
    glVertex3f(-0.5, -0.25, 0.0);
    glVertex3f(0.5, -0.25, 0.0);
    glVertex3f(0.5, 0.5, 0.0);
    glColor3f(0, 1, 0);
    glVertex3f(0.5, 0.25, 0.0);
    glVertex3f(0.9, 0.5, 0.0);
    glVertex3f(0.8, 0.5, 0.0);
    glVertex3f(0.4, 0.25, 0.0);
    glEnd();

    dc.drawCircle(0.25, -0.25, -0.25, 10);
    dc.drawCircle(0.15, 0.25, -0.25, 5);

    glFlush();


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"OpenGL with Python")
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()