from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

GRID_SIZE = 10

class Grid:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.points = []
        glutInit()
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(sizeX * GRID_SIZE, sizeY * GRID_SIZE)
        glutCreateWindow("Raster".encode("ascii"))
        glOrtho(0, sizeX * GRID_SIZE, sizeY * GRID_SIZE, 0, -1, 1)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.end)

    def addPoint(self, x, y, c = 1):
        if 0 <= x < self.sizeX and 0 <= y < self.sizeY:
            x = round(x)
            y = round(y)
            self.points.append((x, y, c))

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        # Draws Points
        for i in self.points:
            x, y, c = i
            if type(c) == tuple:
                glColor(*c)
            else:
                glColor(c, c, c)
            glBegin(GL_POLYGON)
            glVertex(x * GRID_SIZE, y * GRID_SIZE)
            glVertex((x + 1) * GRID_SIZE, y * GRID_SIZE)
            glVertex((x + 1) * GRID_SIZE, (y + 1) * GRID_SIZE)
            glVertex(x * GRID_SIZE, (y + 1) * GRID_SIZE)
            glEnd()
        glColor(.5, .5, .5)
        # Draws Grid
        glBegin(GL_LINES)
        for i in range(1, self.sizeX):
            glVertex(i * GRID_SIZE, 0)
            glVertex(i * GRID_SIZE, self.sizeY * GRID_SIZE)
        for i in range(1, self.sizeY):
            glVertex(0, i * GRID_SIZE)
            glVertex(self.sizeX * GRID_SIZE, i * GRID_SIZE)
        glEnd()
        glBegin(GL_LINES)
        glVertex2i(0,0)
        glVertex2i(10,10)
        glEnd()
        glFlush()

    # Draw a line using Bresenham's algorithm
    def rasterline(self, x1,  y1, x2, y2):
        # Switch (x1,y1) and (x2,y2) if x1 > x2
        if x1 > x2:
            tempx, tempy = x1, y1
            x1, y1 = x2, y2
            x2, y2 = tempx, tempy
        # Calculate delta x and y
        dx = x2 - x1
        dy = y2 - y1
        m = dy/dx
        if m > 0 and m < 1:
            for x in range(x1, x2):
                y = round(m*(x-x1)) + y1
                self.addPoint(x, y)



    def end(self, key, x, y):
        exit()

    def draw(self):
        glutMainLoop()
