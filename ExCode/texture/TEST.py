from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
from OpenGL.GL.shaders import *
import numpy as np

ESCAPE = '\033'
global size
size = 512

def loadImage(imageName) :
    img = Image.open(imageName)
    img_data = np.array(list(img.getdata()), np.uint8)
    return img.size[0], img.size[1], img_data

def drawQuad(B,T,L,R):
    glMultiTexCoord2f(GL_TEXTURE1, 0, 0)
    glBegin(GL_QUADS)
    glMultiTexCoord2f(GL_TEXTURE1, 0.0, 0.0); glMultiTexCoord2f(GL_TEXTURE2, 0.0, 0.0); glVertex3f(B, L,  1.0);       ## Bottom Left Of The Texture and Quad
    glMultiTexCoord2f(GL_TEXTURE1, 1.0, 0.0); glMultiTexCoord2f(GL_TEXTURE2, 1.0, 0.0); glVertex3f( T, L,  1.0);       ## Bottom Right Of The Texture and Quad
    glMultiTexCoord2f(GL_TEXTURE1, 1.0, 1.0); glMultiTexCoord2f(GL_TEXTURE2, 1.0, 1.0); glVertex3f( T,  R,  1.0);       ## Top Right Of The Texture and Quad
    glMultiTexCoord2f(GL_TEXTURE1, 0.0, 1.0); glMultiTexCoord2f(GL_TEXTURE2, 0.0, 1.0); glVertex3f(B,  R,  1.0);       ## Top Left Of The Texture and Quad
    glEnd()

def InitGL(Width, Height):


    if not glUseProgram:
        print('Missing Shader Objects!')
        sys.exit(1)

    global program
    program = compileProgram(
        compileShader('''
                void main()
                {
                    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
                    gl_TexCoord[1] = gl_MultiTexCoord1;
                    gl_TexCoord[2] = gl_MultiTexCoord2;
                }
        ''',GL_VERTEX_SHADER),
        compileShader('''
                uniform sampler2D my_texture1;
                uniform sampler2D my_texture2;
                void main()
                {
                    vec4 color1 = texture2D(my_texture1, gl_TexCoord[1].st);
                    vec4 color2 = texture2D(my_texture2, gl_TexCoord[2].st);
                    if (color1.b > 0.8)
                        discard;
                    gl_FragColor = color1;
                }
    ''',GL_FRAGMENT_SHADER),
    )

    #bmp texture 1
    imagex, imagey, image = loadImage("stone.jpg")
    ix = imagex
    iy = imagey
    glActiveTexture(GL_TEXTURE1)
    global my_texture1
    my_texture1 = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, my_texture1)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glGenerateMipmap(GL_TEXTURE_2D)

    #bmp texture 2
    imagex, imagey, image = loadImage("water.jpg")
    ix = imagex
    iy = imagey
    glActiveTexture(GL_TEXTURE2)
    global my_texture2
    my_texture2 = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, my_texture2)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glGenerateMipmap(GL_TEXTURE_2D)

def DrawGLScene():
    global frame, testvar, my_texture1,my_texture2
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, 0)
    glUseProgram(program)
    myUniformLocation1 = glGetUniformLocation(program, "my_texture1")
    glUniform1i(myUniformLocation1, 1)
    myUniformLocation2 = glGetUniformLocation(program, "my_texture2")
    glUniform1i(myUniformLocation2, 2)
    glViewport(0, 0, size,size)
    glClearDepth(1.0)
    glClearColor (0.0, 0.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -30.0, 30.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    drawQuad(-1.0,1.0,-1.0,1.0)
    glutSwapBuffers()

def keyPressed(*args):
    global texturenumber, shadernumber, frame
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()

def main():
    global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(size,size)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(b"Multitexturing")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(size,size)
    glutMainLoop()

if __name__ == "__main__":
    print("Press 'ESC' key to quit.")
    main()