#include<glad/glad.h>
#include<GLFW/glfw3.h>
#include <iostream>
#include <fstream>
#include<vector>
#include<math.h>

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>

#define STB_IMAGE_IMPLEMENTATION
#include"stb/stb_image.h"




GLuint textura(char fisier[]){
    /*
    functia textura -- creaza un obiect tip textura (varianta simplificata)
    In:
        fisier - fisierul imagine ce contine textura
    Out:
        aliasul (numele) obiectului tip textura incarcat

    Exemplu de utilizare:
        In programul principal:
            _se defineste o variabila GLuint care va lua valori rezultatul acestei functii
            _se precizeaza ce sampler ii corespunde texturii noastre (se face doar odata)
                    glUniform1i(glGetUniformLocation(program, "variabila_textura"), 0);
            _inainte de a desena elementele se face bind pe textura dorita
                    glBindTexture(GL_TEXTURE_2D, alias_textura);

        In fragment shader:
            _definim variabila uniforms variabila_textura
                uniform sampler2D variabila_textura;

            _in functia main vom apela ceva de genul:
                FragColor = texture(variabila_textura, TexCoord);
            unde TexCoord vor fi coordonatele textelilor

    */
    GLuint rezTextura;
    int width, height, nrChannels;

    // cream un obiect de tip textura
    glGenTextures(1, &rezTextura);

    // il legam de contextul curent
    glBindTexture(GL_TEXTURE_2D, rezTextura);

    // definim parametrii ei
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);

    // definim parametrii de filtrare
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

    // load image, create texture and generate mipmaps

    stbi_set_flip_vertically_on_load(true); // facem un flip pe axa Oy

    // incarcam datele din fisierul imagine
    unsigned char *data = stbi_load(fisier, &width, &height, &nrChannels, 0);
    if (data)
    {
        //transferam datele incarcate in obiectul textura
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
        // generam mipmap -uri pentru aceasta textura
        glGenerateMipmap(GL_TEXTURE_2D);
    }
    else
    {
        std::cout << "Failed to load texture" << std::endl;
    }

    //eliberam datele incarcate din fisierul imagine
    stbi_image_free(data);

    //returnam aliasul texturii create
    return rezTextura;

}
