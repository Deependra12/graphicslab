import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from transformation import scaling

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0,-500.0,500.0)


def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.5, 0.5, 0.0)
    glPointSize(5.0)
    glBegin(GL_LINES)

    # X-AXIS (from (-1, 0) to (1, 0))
    glVertex2f(-500.0, 0.0)
    glVertex2f(500.0, 0.0)

    # Y-AXIS (from (0, 1) to (0, -1))
    glVertex2f(0.0, 500.0)
    glVertex2f(0.0, -500.0)
    glEnd()
    glFlush()


    # Drawing Points with coordinate 
    vertice=[(100,200),(300,200),(200,400)]
    xs,ys = scaling(
        vertice,0.5,0.5
    )




    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5.0)
    glBegin(GL_TRIANGLES)
    for vertic in vertice:
        glVertex2f(vertic[0], vertic[1])
        
    glColor3f(1.0, 0.0, 1.0)

    for x,y in zip(xs,ys):
        glVertex2f(x, y)
    glEnd()

    glFlush()



if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("X-AXIS, Y-AXIS Point")
    glutInitWindowSize(500, 500)
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()