import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from winmill_rotation import rotation


fin1 = [[0, 0], [50, -100], [-50, -100]]

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500.0, 500.0,-500.0,500.0)
def draw_polygon(vertices):
    
    glBegin(GL_TRIANGLES)
    for vertic in vertices:
        glVertex2f(vertic[0], vertic[1])
    glEnd()

def draw_windmill():
    base = [[0, 0], [80, -400], [-80, -400]]
    
    global fin1
    glColor3f(1.0, 0.0, 0.0)
    draw_polygon(base)
    glColor3f(1.0, 1.0, 0.0)
    draw_polygon(fin1)
    glColor3f(1.0, 1.0, 0.0)
    fin1 = rotation(
        fin1,120
    )
    
    draw_polygon(fin1)

    glColor3f(1.0, 1.0, 0.0)
    

    fin1 = rotation(
        fin1,120
    )
    

    draw_polygon(fin1)


    fin1 = rotation(
        fin1,0.004
    )
    print(fin1)
    glutPostRedisplay()
    glFlush()




if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow("X-AXIS, Y-AXIS Point")
    glutInitWindowSize(500, 500)
    glutDisplayFunc(draw_windmill)
    init()
    glutMainLoop()