#include "obiect.h"

Obiect::Obiect(int id, std::string const &path, locatie l, rotatie r, scalare s, GLuint &shaderProgram){

    this->idObiect = id;
    this->obj = Model(path);
    this->loc = l;
    this->rotatii.push_back(r);
    this->scal = s;
    this->shaderProgram = shaderProgram;

}

Obiect::Obiect(int id, Obiect sursa, locatie l, rotatie r, scalare s, GLuint &shaderProgram){

    this->idObiect = id;
    this->obj = sursa.getModel();
    this->loc = l;
    this->rotatii.push_back(r);
    this->scal = s;
    this->shaderProgram = shaderProgram;

}

Model Obiect::getModel(){

    return this->obj;
}

int Obiect::getId(){

    return this->idObiect;
}

void Obiect::setLocatie(locatie l){
    this->loc = l;
}

void Obiect::setRotatieInitiala(rotatie r){

    this->rotatii.clear();
    this->rotatii.push_back(r);
}

void Obiect::addRotatie(rotatie r){
    this->rotatii.insert(this->rotatii.begin(), r);
}

void Obiect::setScalare(scalare s){

    this->scal = s;
}

void Obiect::Draw(){

    // se stabileste matricea model si se trimite catre shadere
    glm::mat4 m = glm::mat4(1.0f);
    m = glm::translate(m, glm::vec3(this->loc.x, this->loc.y, this->loc.z));

    for (int i = 0; i < this->rotatii.size(); i++){
            if (this->rotatii[i].unghi != 0)
                m = glm::rotate(m, glm::radians(this->rotatii[i].unghi), glm::vec3(this->rotatii[i].x, this->rotatii[i].y, this->rotatii[i].z));
    }

    m = glm::scale(m, glm::vec3(this->scal.x,this->scal.y,this->scal.z));

    glUniformMatrix4fv(glGetUniformLocation(shaderProgram, "model"), 1, GL_FALSE, &m[0][0]);

    // desenam modelul
    this->obj.Draw(this->shaderProgram);
}

Obiect::~Obiect()
{
    //dtor
}
