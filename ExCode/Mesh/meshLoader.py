from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math


def loadMesh(filename):
    print(filename)
    with open(filename, "rt") as mesh :
        nV = int(next(mesh))
        verts = [[0,0,0] for idx in range(nV)]
        for i in range(0, nV) :
            verts[i][0], verts[i][1], verts[i][2] = [float(x) for x in next(mesh).split()]
        nF = int(next(mesh))
        faces = [[0,0,0] for idx in range(nF)]
        for i in range(0, nF) :
            faces[i][0], faces[i][1], faces[i][2] = [int(x) for x in next(mesh).split()]
    return verts, faces

verts, faces = loadMesh("complex.txt")

def drawVerts(v, f) :
    glBegin(GL_POINTS)
    for i in range(0, len(f)) :
        glVertex3fv(v[f[i][0]])
        glVertex3fv(v[f[i][1]])
        glVertex3fv(v[f[i][2]])
    glEnd()

angle = 0
def disp() :
    global verts, faces, angle
    # reset buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1.0, 0.1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(60, 35, 50, 0, 35, 0, 0, 1, 0)

    angle += 10
    glRotatef(angle, 0,1,0)
    print(angle)
    glColor3f(1,1,1)
    drawVerts(verts, faces)

    #glFlush()
    glutSwapBuffers()


# windowing
if __name__=="__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_DEPTH|GLUT_RGB)
    glutInitWindowSize(512,512)
    glutInitWindowPosition(512,0)
    glutCreateWindow(b"Test Window")
    glClearColor(0, 0.0, 0.0, 0)


    # register callbacks
    glutDisplayFunc(disp)
    glutIdleFunc(disp)


    # enter main infinite-loop
    glutMainLoop()