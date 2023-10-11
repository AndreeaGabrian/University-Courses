# include <GLFW/glfw3.h>
# include <GL/glut.h>
void init ( void )
{
glClearColor (1.0 ,1.0 ,1.0 ,0.0) ;
glMatrixMode ( GL_PROJECTION ) ;
gluOrtho2D (0.0 ,400.0 ,0.0 ,400.0) ;
}
void setPixel ( GLint x , GLint y )
{
glBegin ( GL_POINTS ) ;
glVertex2i (x , y ) ;
glEnd () ;
}
void line ()
{
int x0 = 50 , y0 =50 , xn = 300 , yn = 150 , x , y ;
int dx , dy , // deltas
pk , // decision parameter
k ; // looping variable
glClear ( GL_COLOR_BUFFER_BIT ) ;
glColor3f ( 1 ,0 , 0) ;
setPixel ( x0 , y0 ) ; // plot first point
// difference between starting and ending points
dx = xn - x0 ;
dy = yn - y0 ;
pk = 2 * dy - dx ;
x = x0 ; y = y0 ;
for ( k = 0; k < dx -1; ++ k ) {
if ( pk < 0 ) {
pk = pk + 2 * dy ; // calculate next pk
// next pixel : (x+1 , y )
} else {
// next pixel : (x+1 , y+1)
pk = pk + 2* dy - 2* dx ; // calculate next pk
++ y ;
}
++ x ;
setPixel ( x , y ) ;
}
glFlush () ;
}
int main ( void )
{
GLFWwindow * window ;
/* Initialize the library */
if (! glfwInit () )
return -1;
/* Create a windowed mode window and its OpenGL context */
window = glfwCreateWindow (400 , 400 , " Bresenham ’s Line algorithm , works only for |m| < 1", NULL , NULL ) ;
if (! window )
{
glfwTerminate () ;
return -1;
}
/* Make the w i n d o w s context current */
glfwMakeContextCurrent ( window ) ;
/* set up the initial conditions ( color of the background ), projection mode ,
*/
init () ;
/* Loop until the user closes the window */
while (! glfwWindowShouldClose ( window ) )
{
/* Render here */
line () ;
/* Swap front and back buffers */
glfwSwapBuffers ( window ) ;
/* Poll for and process events */
glfwPollEvents () ;
}
glfwTerminate () ;
return 0;
}
