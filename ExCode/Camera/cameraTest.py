from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


aspRatio = 1.0
camMode = True # True: perspective cam / False: orthographic

def key(c, x, y):
    global camMode

    if c is b'p' :
        camMode = True
    elif c is b'o' :
        camMode = False

    SetCameraProjection(camMode)
    glutPostRedisplay() # draw event!


def SetCameraProjection(perspective) :
    global aspRatio
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if perspective:
        gluPerspective(50,aspRatio,0.1,1000)
    else :
        glOrtho(-2*aspRatio, 2*aspRatio, -2, 2, -1, 1000)

def reshape(neolbi, nopi) :
    global aspRatio, camMode

    aspRatio = neolbi / nopi

    SetCameraProjection(camMode)

    glViewport(0,0, neolbi, nopi)


def disp() :

    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,1,3, 0,0,0, 0,1,0)

    # drawing
    glColor3f(1,1,0)
    glutWireSphere(1.0, 30, 30)
    glTranslatef(0,0,-2)
    glutSolidSphere(1.0, 30, 30)
    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)

glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Camera Test")

## INIT
glClearColor(0, 0.0, 0.0, 0)

# register callbacks
glutDisplayFunc(disp)
glutReshapeFunc(reshape)
glutKeyboardFunc(key)


# enter main infinite-loop
glutMainLoop()