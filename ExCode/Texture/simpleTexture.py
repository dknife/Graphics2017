
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


myTex = [
    [[255, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
    [[255, 255, 255], [255, 0, 255], [255, 255, 255], [255, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [255, 0, 255], [255, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 255]]]


imW = len(myTex[0])
imH = len(myTex)
print(imW, imH)

def GLinit() :
    global imW, imH, myTex
    glClearColor(0.0, 0.0, 0.0, 0)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, imW, imH, 0, GL_RGB,
                 GL_UNSIGNED_BYTE, myTex)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glEnable(GL_TEXTURE_2D)



def myDisp() :
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,1,1)
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3fv([0, 0, 0])
    glTexCoord2f(1,0)
    glVertex3fv([1, 0, 0])
    glTexCoord2f(1, 1)
    glVertex3fv([1, 1, 0])
    glTexCoord2f(0, 1)
    glVertex3fv([0, 1, 0])
    glEnd()
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(100,100)
glutCreateWindow(b"TEXTURE")

GLinit()

glutDisplayFunc(myDisp)
glutMainLoop()