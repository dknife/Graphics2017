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




imgW1, imgH1, myImage1 = loadImage("china.jpg")
imgW2, imgH2, myImage2 = loadImage("spheremap.jpg")

tex = []
nTexture = 2

def CreateTextures() :
    global tex, nTexture, imgW1, imgH1, myImage1, imgW2, imgH2, myImage2

    tex = glGenTextures(nTexture)
    print(tex)

    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, tex[0])
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imgW1, imgH1, 0, GL_RGB, GL_UNSIGNED_BYTE, myImage1)
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
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_STENCIL_TEST)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    CreateTextures()
    glActiveTexture(GL_TEXTURE0)
    glDisable(GL_TEXTURE_GEN_S)
    glDisable(GL_TEXTURE_GEN_T)

    glActiveTexture(GL_TEXTURE1)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)
    glTexGenf(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGenf(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)



angle = 0
def myDisp ():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(-1, 3.0, 5, 0, 0, 0, 0, 1, 0)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 3.0, 5,0])

    angle += 0.1

    glClear(GL_STENCIL_BUFFER_BIT)
    # 주전자  그리기

    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
    glColor3f(1,1,1)
    glPushMatrix()
    glTranslated(0.0, 1.0, 0.0)
    glRotated(angle, 0.0, 0.0, 1.0)
    glutSolidTeapot(0.7)
    glPopMatrix()

    # 거울을 위한 스텐실 영역 설정
    glColorMask(0, 0, 0, 0)
    glDepthMask(0)
    glStencilFunc(GL_ALWAYS, 0x1, 0x1)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.0, 0.0, 2.0)
    glVertex3f(2.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glColorMask(1, 1, 1, 1)
    glDepthMask(1)

    glStencilFunc(GL_EQUAL, 0x1, 0x1)
    # 주전자의 거울상 그리기
    glColor3f(1, 1, 1)
    glPushMatrix()
    glScalef(1.0, -1.0, 1.0)
    glTranslated(0.0, 1.0, 0.0)
    glRotated(angle, 0.0, 0.0, 1.0)
    glutSolidTeapot(0.7)
    glPopMatrix()


    # 거울 그리기
    glDisable(GL_TEXTURE_2D)
    glColor4f(0.5, 0.8, 1.0, 0.5)
    glBegin(GL_TRIANGLES)
    glVertex3f(-2.0, 0.0, 2.0)
    glVertex3f(2.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glEnd()
    glEnable(GL_TEXTURE_2D)

    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH | GLUT_STENCIL | GLUT_RGBA)
glutInitWindowPosition(0,0)
glutInitWindowSize(512,512)
glutCreateWindow(b'Blending')

# initialization
GLinit()


# callback registration
glutDisplayFunc(myDisp)
glutIdleFunc(myDisp)


# enter main loop
glutMainLoop()