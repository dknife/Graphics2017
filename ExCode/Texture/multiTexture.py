from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# install Pilllow package, then you can use PIL
from PIL import Image
import numpy as np

def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data




imgW1, imgH1, myImage1 = loadImage("brightMetal.jpg")
imgW2, imgH2, myImage2 = loadImage("spheremap.jpg")

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
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)

    glActiveTexture(GL_TEXTURE1)
    glBindTexture(GL_TEXTURE_2D, tex[1])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imgW2, imgH2, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myImage2)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glEnable(GL_TEXTURE_2D)




def GLinit() :
    glClearColor(1, 1, 1, 1)
    CreateTextures()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glActiveTexture(GL_TEXTURE0);
    glDisable(GL_TEXTURE_GEN_S);
    glDisable(GL_TEXTURE_GEN_T);
    

    glActiveTexture(GL_TEXTURE1);
    glEnable(GL_TEXTURE_GEN_S);
    glEnable(GL_TEXTURE_GEN_T);
    glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP);
    glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP);

    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1,1,1,1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1,1,1,1])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1,1,1,1])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1,1,1,1])
    glMaterialfv(GL_FRONT, GL_SHININESS, [127.0])


t = 0

def myDisp ():
    global t, tex
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0,2,2, 0,0,0, 0,1,0)

    glLightfv(GL_LIGHT0, GL_POSITION, [0, 1, 1, 0])


    glColor3f(1,1,1)


    t += 0.01
    glRotatef(t, 1,1,1)
    glutSolidTeapot(0.5)

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