# Computer graphics opdracht 3 Tommie Terhoeve 0926280 TI2B
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
        # Define dx,dy
        dx = x2 - x1
        dy = y2 - y1
        if dy < dx:
            if x1 > x2:
                self.bresenham(x2, y2, x1, y1, False)
            else:
                self.bresenham(x1, y1, x2, y2, False)
        else:
            if y1 > y2:
                self.bresenham(x2, y2, x1, y1, True)
            else:
                self.bresenham(x1, y1, x2, y2, True)
    '''
    The algorithm works as follows:
    1. Calculate deltaX and deltaY
    2. If deltaY is bigger than deltaX, switch them around
    3. Check if there is a negative slope, if so the increment needs to be negative
    4. Calculate D (difference) Which is the distance of the line to the center of the pixel.
    5. If switched calculate the next X coordinate for every Y coordinate
    6. If not switched calculate the next Y coordinate for every X coordinate
    '''

    def bresenham(self, x1, y1, x2, y2, isSwitched):
        # Define dx,dy
        dx = x2 - x1
        dy = y2 - y1
        if isSwitched:
            temp = dx
            dx = dy
            dy = temp
        yi = 1
        # If there is a negative slope
        if dy < 0:
            yi = - 1
            dy = -dy
        D = 2*dy - dx
        if isSwitched:
            x = x1
            for y in range(y1, y2 + 1):
                self.addPoint(x, y)
                # If D is positive, increment x
                if D > 0:
                    x = x + yi
                    D = D - 2*dx
                D = D + 2*dy
        else:
            y = y1
            for x in range(x1, x2 + 1):
                    self.addPoint(x, y)
                    # If D is positive, increment y
                    if D > 0:
                        y = y + yi
                        D = D - 2*dx
                    D = D + 2*dy

    def end(self, key, x, y):
        exit()

    def draw(self):
        glutMainLoop()
