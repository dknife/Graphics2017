from OpenGL.GLUT import *
from OpenGL.GL import *
import math

twopi = 3.14*2.0

def drawCircle(radius, dx, dy, nPoints=100) :

    nPoints = 100
    angle = 0.0
    angleStep = twopi / nPoints

    glBegin(GL_POLYGON)
    for i in range(0, nPoints):
        glVertex3f(radius*math.cos(angle) + dx, radius*math.sin(angle) + dy, 0)
        angle += angleStep

    glEnd()