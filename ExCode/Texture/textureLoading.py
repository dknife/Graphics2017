from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy
from PIL import Image


def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = numpy.array(list(img.getdata()), numpy.uint8)
    return img.size[0], img.size[1], img_data

def GLinit() :
    glClearColor(0, 0.0, 0.0, 0)
    ix, iy, img = loadImage('tiger2.bmp')
    im = glGenTextures(1, img)
    glBindTexture(GL_TEXTURE_2D, im)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, img)
    glEnable(GL_TEXTURE_2D)

angle = 0

def disp() :
    global angle
    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.1,1.1,-1.1,1.1,-10,10)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    angle += 0.1
    glRotatef(angle, 1,1,1)
    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glTexCoord2fv([0, 0])
    glVertex3fv([-1, 1, 0])
    glTexCoord2fv([0, 1])
    glVertex3fv([-1,-1, 0])
    glTexCoord2fv([1, 1])
    glVertex3fv([ 1,-1, 0])
    glTexCoord2fv([1, 0])
    glVertex3fv([ 1, 1, 0])
    glEnd()

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_DEPTH|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

GLinit()



# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)

# enter main infinite-loop
glutMainLoop()