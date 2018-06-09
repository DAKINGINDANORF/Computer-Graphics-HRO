from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Game():
    # Tuples representing the verticies of the shape
    verticies = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )

    # Edges representing the lines between verticies
    edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
        )

    # Surfaces on the shape (this enables us to color in the surfaces)
    surfaces = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6),
        )

    # Initialises GLUT and creates a window
    def __init__(self, width, height):
        # Initialises GLUT
        glutInit(sys.argv)
        # Creates a window
        glutInitWindowPosition(100,100)
        glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
        glutInitWindowSize(width,height)
        glutCreateWindow("Demo eindopdracht")
        # Tell GLUT to run function whenever update is requested
        glutDisplayFunc(self.render_scene)
        # Go into GLUT event processing main loop
        glutMainLoop()

    def render_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glVertex3f(-2,-2,-5.0)
        glVertex3f(2,0.0,-5.0)
        glVertex3f(0.0,2,-5.0)
        glEnd()
        glutSwapBuffers()


game = Game(320,320)
