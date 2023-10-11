#include "scena.h"

Scena::Scena()
{
    //ctor
}

void Scena::addObiect(Obiect o){
    this->listaObiecte.push_back(o);
}

void Scena::addRotatieObiect(int idObj, rotatie r){
    //returneaza indicele cu idObj-ul dat ca input sau ridica o exceptie
    int aux = -1;
    for(int i = 0; i < this->listaObiecte.size(); i++)
        if (this->listaObiecte[i].getId() == idObj){
            aux = i;
        }
    if (aux == -1) throw 20;
    this->listaObiecte[aux].addRotatie(r);
}

Obiect Scena::getObiect(int idObj){

    //returneaza obiectul cu idObj-ul dat ca input sau ridica o exceptie
    for(int i = 0; i < this->listaObiecte.size(); i++)
        if (this->listaObiecte[i].getId() == idObj){
            return this->listaObiecte[i];
        }
    throw 20;
}

void Scena::DrawScene(){
    for(int i=0; i<this->listaObiecte.size();i++){
        this->listaObiecte[i].Draw();
    }
}




Scena::~Scena()
{
    //dtor
}
