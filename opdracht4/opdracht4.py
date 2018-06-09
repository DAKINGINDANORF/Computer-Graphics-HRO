from lines import *
import math
import time

# Renders in Isometric perspective
class Render:
    # Render a 640*480 window
    l = Lines(1000, 500)

    # Matrix-vector multiplication
    def multiply_matrix_vector(self,matrix, vector):
    	multiplied_matrix = [0] * len(matrix)
    	if len(matrix[0]) == len(vector):
            # loops through columns of matrix
    		for i in range (0, len(matrix)):
                # Loops through vector and rows of matrix
    			for j in range(0, len(vector)):
                    # Multiplies matrix coordinate with vector
    				multiplied_matrix[i] += matrix[i][j] * vector[j]
    	return multiplied_matrix

    # Converts 3D coordinate to isometric (Ax,Ay,Az) coordinate
    def to_isometric(self, coordinate_list, rotation):
        isometric_coordinates = []
        alpha = math.asin(math.tan(math.radians(30)))
        beta = math.radians(45 + rotation)
        projection_matrix_one = ((math.cos(beta), 0, -1 * math.sin(beta)),
        						 (0, 1, 0),
        						 (math.sin(beta), 0, math.cos(beta)))
        projection_matrix_two = ((1, 0, 0),
        			  			(0, math.cos(alpha), math.sin(alpha)),
        			  			(0, -1 * math.sin(alpha), math.cos(alpha)))
        for coordinate in coordinate_list:
        	first_matrix_calc = self.multiply_matrix_vector(projection_matrix_one, coordinate)
        	second_matrix_calc =self.multiply_matrix_vector(projection_matrix_two, first_matrix_calc)
        	isometric_coordinates.append((second_matrix_calc[0] + 500, second_matrix_calc[1] + 250))
        return isometric_coordinates

    # Draws cube using x,y coordinate of isometric-coordinate
    def drawCube(self, isometric_coordinates, edges):
    	for edge in edges:
            # Draw a line between coordinates using edges
    		self.l.addLine(isometric_coordinates[edge[0]], isometric_coordinates[edge[1]])

    # Renders the line and draws the field
    def run(self, rotation):
        cube = Cube(0, 0, 0, -200)
        points = cube.return_vertex_coordinates()
        points2 = self.to_isometric(points, rotation)
        self.drawCube(points2, cube.return_edges())
        self.l.draw()


class Cube():

	# vertices related (0,0,0)
	vertices = [[-1, -1, -1],
			   [1, -1, -1],
			   [1, 1, -1],
			   [-1, 1, -1],
			   [-1, -1, 1],
			   [1, -1, 1],
			   [1, 1, 1],
			   [-1, 1, 1]]

    # Edges of cube which attach to eachother creating lines
	edges = ((0, 1),
			(1, 2),
			(2, 3),
			(0, 3),
			(0, 4),
			(1, 5),
			(2, 6),
			(3, 7),
			(4, 5),
			(5, 6),
			(6, 7),
			(4, 7))

    # Constructor
	def __init__(self, x, y, z, s):
		self.x = x # x coordinate
		self.y = y # y coordinate
		self.z = z # z coordinate
		self.s = s # s (scale)

	# Converts vertices to coordinates in the world
	def return_vertex_coordinates(self):
		return_coordinates = []
		for vertex in self.vertices:
			new_x = vertex[0] * 0.5 * self.s + self.x
			new_y = vertex[1] * 0.5 * self.s + self.y
			new_z = vertex[2] * 0.5 * self.s + self.z
			return_coordinates.append((new_x, new_y, new_z))
		return return_coordinates

    # Returns edges, used in calculations
	def return_edges(self):
		return self.edges

r = Render()
# Parse angle of rotation as parameter
# When using Isometric-projection there is no need for a seperate rotation matrix
r.run(30)
