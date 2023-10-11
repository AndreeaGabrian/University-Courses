#ifndef OBIECT_H
#define OBIECT_H
#include "model.h"
#include<iostream>

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

// structuri folosite pentru a construi matricea model
struct locatie{
    float x, y, z;
};

struct rotatie{
    float unghi, x, y, z;
};

struct scalare{
    float x, y, z;
};

class Obiect
{
    public:

        // constructori
        Obiect(int id, std::string const &path, locatie l, rotatie r, scalare s, GLuint &shaderProgram);
        Obiect(int id, Obiect sursa, locatie l, rotatie r, scalare s, GLuint &shaderProgram);

        // set-eri si get-eri
        Model getModel();
        int getId();

        void setLocatie(locatie l);

        // reinitializam vectorul cu rotatii (se sterg toate rotatiile, si se pune doar rotatia ca argument)
        void setRotatieInitiala(rotatie r);
        // adaugam o rotatie
        void addRotatie(rotatie r);
        void setScalare(scalare s);

        // functia de desenare
        void Draw();

        // destructori
        virtual ~Obiect();

    private:
        int idObiect;
        Model obj;

        std::vector<rotatie> rotatii;
        scalare scal;
        locatie loc;

        GLuint shaderProgram;
};

#endif // OBIECT_H
