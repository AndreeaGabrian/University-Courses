#ifndef SCENA_H
#define SCENA_H
#include "obiect.h"
#include<iostream>

class Scena
{
    public:
        Scena();
        virtual ~Scena();

        Obiect getObiect(int idObj);
        void addObiect(Obiect o);
        void addRotatieObiect(int idObj, rotatie r);
        void DrawScene();

    private:
        std::vector<Obiect> listaObiecte;

};

#endif // SCENA_H
