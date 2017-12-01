from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

# 할일
# 1. 조명을 사용하게 설정 : glEnable(GL_LIGHTING)
# 2. GL_LIGHT0~ n개의 조명 : 몇 개를 쓸 것인가? : glEnable(GL_LIGHT0)
# 3. 조명의 색을 결정 : glLightfv(GL_LIGHT0, ...)
# 4. 재질의 색을 결정 : glMaterialfv
# 5. 조명의 위치를 잡는다: glLightfv(GL_LIGHT0, POSITION...)

L_diffuse = [1.0, 1.0, 1.0, 1.0] # r, g, b, alpha
L_specular= [1.0, 1.0, 1.0, 1.0]
L_ambient = [0.1, 0.1, 0.1, 1.0]

M_shininess = [127.0]
M_diffuse = [0.0, 1.0, 0.0, 1.0]
M_specular= [1.0, 1.0, 0.0, 1.0]
M_ambient = [0.0, 0.5, 0.0, 1.0]

L_position = [1.0, 2.0, 1.0, 1.0]
time = 0

def reshape(w,h) :
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, w/h, 0.1, 1000)
    glViewport(0,0,w,h)


def disp() :
    global L_position, time

    time += 0.001
    L_position[0] = math.sin(time)
    L_position[2] = math.cos(time)
    M_shininess[0] = math.fabs(117.0*math.sin(time))+10.0
    glMaterialfv(GL_FRONT, GL_SHININESS, M_shininess)

    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    # light position
    glLightfv(GL_LIGHT0, GL_POSITION, L_position)
    glutSolidSphere(1.0, 30,28) #Teapot(1.0)
    glFlush()


# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_DEPTH|GLUT_RGB)
glutInitWindowSize(512,512)
glutInitWindowPosition(512,0)
glutCreateWindow(b"Test Window")

# initialization
glClearColor(0, 0.0, 0.0, 0)
glShadeModel(GL_FLAT)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_DIFFUSE, L_diffuse)
glLightfv(GL_LIGHT0, GL_SPECULAR, L_specular)
glLightfv(GL_LIGHT0, GL_AMBIENT, L_ambient)

glMaterialfv(GL_FRONT, GL_DIFFUSE, M_diffuse)
glMaterialfv(GL_FRONT, GL_SPECULAR, M_specular)
glMaterialfv(GL_FRONT, GL_AMBIENT, M_ambient)
glMaterialfv(GL_FRONT, GL_SHININESS, M_shininess)


# register callbacks
glutDisplayFunc(disp)
glutIdleFunc(disp)
glutReshapeFunc(reshape)

# enter main infinite-loop
glutMainLoop()