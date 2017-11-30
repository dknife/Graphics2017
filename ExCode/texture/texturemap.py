from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np
import math

def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data




imgW1, imgH1, myImage1 = loadImage("stone.jpg")
imgW2, imgH2, myImage2 = loadImage("water.jpg")

tex = []
nTexture = 2

def CreateTextures() :
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




def GLinit() :
    print("Vendor:   " , glGetString(GL_VENDOR))
    print("Renderer: " , glGetString(GL_RENDERER))
    print("OpenGL Version:  " , glGetString(GL_VERSION))
    print("Shader Version:  " , glGetString(GL_SHADING_LANGUAGE_VERSION))

    glClearColor(0, 0, 0, 1)
    CreateTextures()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    # meaningless call to avoid "invalid operation" error of glEnd()
    glMultiTexCoord2f(GL_TEXTURE1, 0, 0)


t = 0

def myDisp ():
    global t, tex
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0,0,2, 0,0,0, 0,1,0)

    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 1, 0])


    glColor3f(1,1,1)


    t += 0.001
    glRotatef(t, 1,1,1)

    glActiveTexture(GL_TEXTURE1)
    glMatrixMode(GL_TEXTURE)
    glLoadIdentity()
    glTranslatef(t,0,0)

    mag = 0.01
    f = 20.0
    c = mag*math.cos(f*t)
    s = mag*math.sin(2*f*t)

    glBegin(GL_QUADS)
    glTexCoord2f(s,s)
    glMultiTexCoord2f(GL_TEXTURE1, 0,0)
    glVertex2f(-1,1)
    glTexCoord2f(0+s, 3+c)
    glMultiTexCoord2f(GL_TEXTURE1, 0,1)
    glVertex2f(-1,-1)
    glTexCoord2f(3+c, 3+s)
    glMultiTexCoord2f(GL_TEXTURE1, 1,1)
    glVertex2f( 1,-1)
    glTexCoord2f(3+c, 0+c)
    glMultiTexCoord2f(GL_TEXTURE1, 1,0)
    glVertex2f( 1, 1)
    glEnd()

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(512,512)
glutCreateWindow(b'my texture')

# initialization
GLinit()


# callback registration
glutDisplayFunc(myDisp)
glutIdleFunc(myDisp)


# enter main loop
glutMainLoop()