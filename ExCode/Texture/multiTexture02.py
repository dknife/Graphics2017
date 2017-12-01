from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np
import math


def loadImage(imageName):
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data


imgW1, imgH1, myImage1 = loadImage("pebbles.jpg")
imgW2, imgH2, myImage2 = loadImage("water.jpg")

tex = []
nTexture = 2


def CreateTextures():
    global tex, nTexture, imgW1, imgH1, myImage1, imgW2, imgH2, myImage2

    tex = glGenTextures(nTexture)
    print(tex)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, tex[0])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imgW1, imgH1, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage1)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

    glActiveTexture(GL_TEXTURE1)
    glBindTexture(GL_TEXTURE_2D, tex[1])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imgW2, imgH2, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage2)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)


def GLinit():
    glClearColor(1, 1, 1, 1)
    CreateTextures()
    glEnable(GL_DEPTH_TEST)
    glMultiTexCoord2f(GL_TEXTURE0, 0, 0)


t = 0

def myDisp():
    global t, tex
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)

    glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 1, 0])

    glColor3f(1, 1, 1)


    t += 0.001
    glActiveTexture(GL_TEXTURE1)
    glMatrixMode(GL_TEXTURE)
    glLoadIdentity()
    glTranslatef(t,0,0)

    glBegin(GL_QUADS)
    glMultiTexCoord2f(GL_TEXTURE0, 0.01*math.sin(t*10.0), 0)
    glMultiTexCoord2f(GL_TEXTURE1, 0, 0)
    glVertex3f(-1, 1, 0)
    glMultiTexCoord2f(GL_TEXTURE0, 0.01*math.cos(t*10.0), 1+0.01*math.cos(t*10.0))
    glMultiTexCoord2f(GL_TEXTURE1, 0, 1)
    glVertex3f(-1,-1, 0)
    glMultiTexCoord2f(GL_TEXTURE0, 1, 1+0.01*math.sin(t*10.0))
    glMultiTexCoord2f(GL_TEXTURE1, 1, 1)
    glVertex3f( 1,-1, 0)
    glMultiTexCoord2f(GL_TEXTURE0, 1+0.01*math.cos(t*10.0), 0.01*math.sin(t*10.0))
    glMultiTexCoord2f(GL_TEXTURE1, 1, 0)
    glVertex3f( 1, 1, 0)
    glEnd()

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowPosition(0, 0)
glutInitWindowSize(512, 512)
glutCreateWindow(b'my texture')

# initialization
GLinit()

# callback registration
glutDisplayFunc(myDisp)
glutIdleFunc(myDisp)

# enter main loop
glutMainLoop()