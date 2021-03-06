// Eindopdracht Computer graphics 

#include "stdafx.h"
#include <windows.h>  // for MS Windows
#include <GL/freeglut.h>  // GLUT, include glu.h and gl.h

/* Global variables */
float angleY = 0.0f;
float angleZ = 0.0f;
bool animationEnabled = false;
GLfloat LightPosition[] = { 1.0, 1.0, 1.0, 0.0 };
/* Initialises lightning */
void initLightning(void)
{
	GLfloat mat_specular[] = { 0.7, 0.7, 0.7, 0.7 };
	GLfloat mat_shininess[] = { 10.0 };
	glClearColor(1, 1, 1, 1);
	glShadeModel(GL_SMOOTH);
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
	glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess);
	glEnable(GL_LIGHTING);
	glEnable(GL_LIGHT0);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_COLOR_MATERIAL);
}
/* Changes size without distorting image*/
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
	case 'q':
		animationEnabled = !animationEnabled;
		return;
	}
}
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
	/* Putting method here prevents lightning from rotating with object */
	glLightfv(GL_LIGHT0, GL_POSITION, LightPosition);
	/* Draw a cube using QUAD polygons*/

	/* Top */
	glBegin(GL_QUADS);
	glColor3f(0.8f, 0.3f, 0.8f);
	glVertex3f(1.0f, 1.0f, -1.0f);
	glVertex3f(-1.0f, 1.0f, -1.0f);
	glVertex3f(-1.0f, 1.0f, 1.0f);
	glVertex3f(1.0f, 1.0f, 1.0f);

	/* Bottom */
	glColor3f(1.0f, 0.0f, 0.0f);
	glVertex3f(1.0f, -1.0f, 1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(1.0f, -1.0f, -1.0f);

	/* Front */
	glColor3f(1.0f, 0.2f, 0.8f);
	glVertex3f(1.0f, 1.0f, 1.0f);
	glVertex3f(-1.0f, 1.0f, 1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, 1.0f);

	/* Back */
	glColor3f(0.0f, 1.0f, 0.1f);
	glVertex3f(1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, 1.0f, -1.0f);
	glVertex3f(1.0f, 1.0f, -1.0f);

	/* Left */
	glColor3f(1.0f, 0.6f, 1.0f);
	glVertex3f(-1.0f, 1.0f, 1.0f);
	glVertex3f(-1.0f, 1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);

	/* Right */
	glColor3f(0.0f, 1.0f, 1.0f);
	glVertex3f(1.0f, 1.0f, -1.0f);
	glVertex3f(1.0f, 1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, -1.0f);
	glEnd();  // End of drawing color-cube
	glutSwapBuffers();

	/* If the user enables the automatic rotation */
	if (animationEnabled) {
		angleY += 5;
		angleZ += 5;
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
	/* Lightning settings */
	initLightning();
	/* Enter GLUT main event handler loop */
	glutMainLoop();
	return 1;
}
