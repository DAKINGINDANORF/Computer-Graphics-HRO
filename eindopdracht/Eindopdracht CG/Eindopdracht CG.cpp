// Eindopdracht Computer graphics 

#include "stdafx.h"
#include <windows.h>  // for MS Windows
#include <GL/freeglut.h>  // GLUT, include glu.h and gl.h

/* Global variables */
float angleY = 0.0f;
float angleZ = 0.0f;

/* Changes size without distorting image*/
void changeSize(int width, int height) {

	/* Prevents a divide by zero when calculating aspect ratio*/
	if (height == 0)
		height = 1;
	float ratio = 1.0* width / height;

	/* Use a projection matrix */
	glMatrixMode(GL_PROJECTION);
	/* Resets matrix */
	glLoadIdentity();
	/* Sets the viewport to be the entire window*/
	glViewport(0, 0, width, height);
	/* Sets the Field of View*/
	gluPerspective(45, ratio, 1, 100);
	/* For safety we set matrix mode back to GL_Modelview*/
	glMatrixMode(GL_MODELVIEW);
}

/* Is called by GLUT to render the shape*/
void renderScene() {
	/* Clears color and depth buffers */
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	/* Resets transformations */
	glLoadIdentity();
	/* Tells the camera where to look at*/
	gluLookAt
		/* Position */
		(0.0f, 0.0f, 5.0f,
			/* Target to look at*/
			0.0f, 0.0f, 0.0f,
			/* Angle */
			0.0f, 10.0f, 0.0f);
	/* Rotate on Y axis */
	glRotatef(angleY, 0.0f, 1.0f, 0.0f);
	/* Rotate on Z axis */
	glRotatef(angleZ, 0.0f, 0.0, 1.0f);
	/* Draw a cube using QUAD polygons*/
	// Top face (y = 1.0f)
	glBegin(GL_QUADS);
	glColor3f(0.0f, 1.0f, 0.0f);
	glVertex3f(1.0f, 1.0f, -1.0f);
	glVertex3f(-1.0f, 1.0f, -1.0f);
	glVertex3f(-1.0f, 1.0f, 1.0f);
	glVertex3f(1.0f, 1.0f, 1.0f);

	// Bottom face (y = -1.0f)
	glColor3f(1.0f, 0.5f, 0.0f);     // Orange
	glVertex3f(1.0f, -1.0f, 1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(1.0f, -1.0f, -1.0f);

	// Front face  (z = 1.0f)
	glColor3f(1.0f, 0.0f, 0.0f);     // Red
	glVertex3f(1.0f, 1.0f, 1.0f);
	glVertex3f(-1.0f, 1.0f, 1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, 1.0f);

	// Back face (z = -1.0f)
	glColor3f(1.0f, 1.0f, 0.0f);     // Yellow
	glVertex3f(1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, 1.0f, -1.0f);
	glVertex3f(1.0f, 1.0f, -1.0f);

	// Left face (x = -1.0f)
	glColor3f(0.0f, 0.0f, 1.0f);     // Blue
	glVertex3f(-1.0f, 1.0f, 1.0f);
	glVertex3f(-1.0f, 1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);

	// Right face (x = 1.0f)
	glColor3f(1.0f, 0.0f, 1.0f);     // Magenta
	glVertex3f(1.0f, 1.0f, -1.0f);
	glVertex3f(1.0f, 1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, -1.0f);
	glEnd();  // End of drawing color-cube
	glutSwapBuffers();
}

void keyboardHandler(unsigned char key, int x, int y) {
	switch (key) {
	case 'w':
		angleY += 30.0f;
		return;
	case 's':
		angleY -= 30.0f;
		return;
	case 'a':
		angleZ -= 30.0f;
		return;
	case 'd':
		angleZ += 30.0f;
		return;
	}
}
/* Initialises GLUT */
int main(int argc, char **argv) {
	/* Functions to initialise a GLUT window*/
	glutInit(&argc, argv);
	glutInitWindowPosition(10, 10);
	glutInitWindowSize(400, 400);
	/* Double buffer window required for smooth animations*/
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);
	glutCreateWindow("Computer Graphics eindopdracht");
	/* Tells GLUT which function to display*/
	glutDisplayFunc(renderScene);
	/* Enables window to be resized without distorting shape */
	glutReshapeFunc(changeSize);
	/* Calls function when application is in idle (no input) */
	glutIdleFunc(renderScene);
	/* Process keyboard input */
	glutKeyboardFunc(keyboardHandler);
	/* Enter GLUT main event handler loop */
	glutMainLoop();
	return 1;
}
