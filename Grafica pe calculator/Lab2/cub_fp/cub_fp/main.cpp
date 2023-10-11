# include <GLFW/glfw3.h>
# include <GL/glut.h>
#include <unistd.h>
#include <math.h>

float verticies[8][3] = {
    { 1.0, -1.0, -1.0},
    { 1.0,  1.0, -1.0},
    {-1.0,  1.0, -1.0},
    {-1.0, -1.0, -1.0},
    { 1.0, -1.0,  1.0},
    { 1.0,  1.0,  1.0},
    {-1.0, -1.0,  1.0},
    {-1.0,  1.0,  1.0}
    };

int edges[12][2] = {
    {0, 1},
    {0, 3},
    {0, 4},
    {2, 1},
    {2, 3},
    {2, 7},
    {6, 3},
    {6, 4},
    {6, 7},
    {5, 1},
    {5, 4},
    {5, 7}
    };

int surfaces[6][4] = {
    {0, 1, 2, 3},
    {3, 2, 7, 6},
    {6, 7, 5, 4},
    {4, 5, 1, 0},
    {1, 5, 7, 2},
    {4, 0, 3, 6}
    };


float colors[12][3] = {
    {1.0, 0.0, 0.0},
    {0.0, 1.0, 0.0},
    {0.0, 0.0, 1.0},
    {0.0, 1.0, 0.0},
    {1.0, 1.0, 1.0},
    {0.0, 1.0, 1.0},
    {1.0, 0.0, 0.0},
    {0.0, 1.0, 0.0},
    {0.0, 0.0, 1.0},
    {1.0, 0.0, 0.0},
    {1.0, 1.0, 1.0},
    {0.0, 1.0, 1.0},
    };

int display[2]={400, 400};


void init ( void ){

    // openGL va ascunde suprafetele ce vor fi specificate
    glEnable(GL_CULL_FACE);
    // specificam sa se ascunda pe cele din spate
    glCullFace(GL_BACK);
    // precizam ordinea in care sunt desenate (invers acelor de ceasornic e default) --
    glFrontFace(GL_CW);

    // precizam ca aspura carei matrici vom stabili parametrii (in acest caz asupra matricii de proiectie)
    glMatrixMode( GL_PROJECTION );

    // stabilim perspectiva
    gluPerspective(45, (display[0]/display[1]), 0.0, 50.0);
    // culoarea fundalului
    glClearColor (0.0 ,0.0 ,0.0 ,0.0) ;
    // mutam camera in spate cu 10 unitati ca sa vedem mai bine cubul
    glTranslatef(0, 0, -10);
    glRotatef(60, 0, 1, 1);
}


void cubeFull( void ){
    int indexSurface, indexVertex;

    glBegin(GL_QUADS);

    for(indexSurface = 0; indexSurface < 6; indexSurface++)
        for(indexVertex = 0; indexVertex < 4; indexVertex++){
                glColor3f(colors[surfaces[indexSurface][indexVertex]][0],colors[surfaces[indexSurface][indexVertex]][1],colors[surfaces[indexSurface][indexVertex]][2]);
                glVertex3f(verticies[surfaces[indexSurface][indexVertex]][0],verticies[surfaces[indexSurface][indexVertex]][1],verticies[surfaces[indexSurface][indexVertex]][2]);
        }
    glEnd();


    glFlush ();
}


 int main ( void )
 {
    GLFWwindow * window ;
    /* Initializam libraria */
    if (! glfwInit ())
        return -1;

    /* Cream o fereastra si ii atasam un context OpenGL */
    window = glfwCreateWindow (display[0], display[1] , "Cube fixed pipeline!", NULL , NULL );
    if (! window )
    {
        glfwTerminate ();
        return -1;
    }

    /* Facem fereastra curenta contextul curent */
    glfwMakeContextCurrent ( window );

    /* se initializeaza conditiile initiale, projection mode, etc. */
    init();


    /* Loop pana cand se inchide fereastra */
    while (! glfwWindowShouldClose ( window ))
    {

        /* Aici se desenează */
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);

        //glPushMatrix();
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE); // comentati linia daca vreti sa desenati cubul plin

        cubeFull();

        //glMatrixMode( GL_MODELVIEW );
        glRotatef(10, 1, 4, 1);
        //glPopMatrix();

        /* Se inverseaza bufferele */
        glfwSwapBuffers ( window );

        /* intarziem putin ca sa putem sa vedem rotatia */
        usleep(100000);

        /* Procesam evenimentelele */
        glfwPollEvents ();
    }

    glfwTerminate ();
    return 0;
 }
