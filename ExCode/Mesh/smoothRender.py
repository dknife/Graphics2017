from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import numpy as np
import Shader as sc


# Light Properties
Ld = [1,1,1,1]
Ls = [1,1,1,1]
# Material Properties
Md = [0.6,0.8,0,1]
Ms = [1,1,1,1]
shininess = [0]

t = 0



# initialization
def GLinit() :

    glClearColor(0,0,0,0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, Ld)
    glLightfv(GL_LIGHT0, GL_SPECULAR, Ls)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, Md)
    glMaterialfv(GL_FRONT, GL_SPECULAR, Ms)
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)


def computeNormal(p1, p2, p3) :
    u = np.array([p2[i] - p1[i] for i in range(0, 3)])
    v = np.array([p3[i] - p1[i] for i in range(0, 3)])
    N = np.cross(u,v)
    return N


def loadMesh(filename):
    print(filename)
    with open(filename, "rt") as mesh :
        nV = int(next(mesh))
        verts = [[0,0,0] for idx in range(nV)]
        normals = np.array([[0.0, 0.0, 0.0] for idx in range(nV)])
        for i in range(0, nV) :
            verts[i][0], verts[i][1], verts[i][2] = [float(x) for x in next(mesh).split()]
        nF = int(next(mesh))
        faces = [[0,0,0] for idx in range(nF)]
        for i in range(0, nF) :
            faces[i][0], faces[i][1], faces[i][2] = [int(x) for x in next(mesh).split()]
            Normal = computeNormal(verts[faces[i][0]],verts[faces[i][1]],verts[faces[i][2]])

            for points in range(3) :
                normals[faces[i][points]] = normals[faces[i][points]] + Normal


        for i in range(0, nV):
            len = np.linalg.norm(normals[i])
            if len > 0.000001 :
                normals[i] = normals[i]/len


    return verts, faces, normals

V1, F1, N1 = loadMesh("complex.txt")
V2, F2, N2 = loadMesh("cloth.txt")

def flatten(x) :
    flattenArray = []
    for lists in x :
        for elements in lists :
            flattenArray.append(elements)
    return flattenArray


vertices = flatten(V1)
faces = flatten(F1)
normals = flatten(N1)

vertices2 = flatten(V2)
faces2 = flatten(F2)
normals2 = flatten(N2)




shader=None
buffers1 = None
buffers2 = None


def create_vbo(v, n, f):
    buffers = glGenBuffers(3)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
    glBufferData(GL_ARRAY_BUFFER,
            len(v)*4,  # byte size
            (ctypes.c_float*len(v))(*v),
            GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
    glBufferData(GL_ARRAY_BUFFER,
            len(n)*4, # byte size
            (ctypes.c_float*len(n))(*n),
            GL_STATIC_DRAW)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2])
    glBufferData(GL_ELEMENT_ARRAY_BUFFER,
            len(f)*4, # byte size
            (ctypes.c_uint*len(f))(*f),
            GL_STATIC_DRAW)
    return buffers


def draw_vbo(buffers, f):
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_NORMAL_ARRAY);
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0]);
    glVertexPointer(3, GL_FLOAT, 0, None);
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1]);
    glNormalPointer(GL_FLOAT, 0, None);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2]);
    glDrawElements(GL_TRIANGLES, len(f), GL_UNSIGNED_INT, None);
    glDisableClientState(GL_NORMAL_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY);



def drawMeshWithShader(buffers, f):
    draw_vbo(buffers, f)



# display callback
def display() :
    global t, shader, V1, F1, N1, vertices, normals, faces, vertices2, normals2, faces2, buffers1, buffers2

    if shader==None:
        shader=sc.Shader()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # CAMERA SETTING
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,40,60, 0,40,0, 0,1,0)

    t += 0.1
    glRotatef(t, 0,1,0)
    glLightfv(GL_LIGHT0, GL_POSITION, [math.sin(t),1,0,0])


    glColor3f(1,0.8, 0.9)
    shininess = [5]
    glMaterialfv(GL_FRONT, GL_SHININESS, shininess)

    shader.begin()

    if buffers1 is None :
        buffers1 = create_vbo(vertices, normals, faces)
    if buffers2 is None :
        buffers2 = create_vbo(vertices2, normals2, faces2)

    glColor3f(1,1,1)
    drawMeshWithShader(buffers1, faces)
    glColor3f(1.0, 0.7, 0.7)
    glPushMatrix()
    glScalef(1.02,1.0,1.02)
    drawMeshWithShader(buffers2, faces2)
    glPopMatrix()

    shader.end()


    glFlush()

# windowing
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_DEPTH |GLUT_RGBA)
glutInitWindowSize(600,600)
glutInitWindowPosition(10,10)
glutCreateWindow(b"Light on Triangles")


GLinit()

# register callbacks
glutDisplayFunc(display)
glutIdleFunc(display)

# enter main-loop
glutMainLoop()