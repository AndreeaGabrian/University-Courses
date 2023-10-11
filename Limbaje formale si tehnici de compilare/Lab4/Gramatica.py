import json

EPSILON = "epsilon"


class Gramatica:

    def __init__(self, non_terminale:list, terminale:list, productii:dict, simbol_start):
        self.__non_terminale = non_terminale
        self.__terminale = terminale
        self.__productii = productii
        self.__simbol_start = simbol_start

    def get_non_terminale(self):
        return self.__non_terminale

    def get_terminale(self):
        return self.__terminale

    def get_productii(self):
        return self.__productii

    def get_simbol_start(self):
        return self.__simbol_start

    def verifica_daca_este_regulara(self):
        """
        Verifica daca gramatica este regulara.
        O greamatica este regulara daca este liniara la dreapta si singurul non-terminal care
        poate merge in epsilon este simbolul de start. In acest caz simbolul de start nu mai apare
        in partea dreapta a niciunei productii
        :return: True daca gramatica este regulara, False altfel
        """
        exista_epsilon_start = False
        exista_simbol_start_in_dreapta = False
        este_liniara_la_dreapta = True

        for (key, values) in self.__productii.items():
            #verificare liniaritate la dreapta
            for elem in values:
                if len(elem) > 2:
                    este_liniara_la_dreapta = False
                if len(elem) == 1:
                    if elem not in self.__terminale:
                        este_liniara_la_dreapta = False
                if len(elem) == 2:
                    if elem[0] not in self.__terminale and elem[1] not in self.__non_terminale:
                        este_liniara_la_dreapta = False
            #------------

                #verificare productii cu epsilon
                if self.__simbol_start in elem:
                    exista_simbol_start_in_dreapta = True

            if EPSILON in values:
                if key != self.__simbol_start:
                    return False
                else:
                    exista_epsilon_start = True
                #--------------

            if exista_epsilon_start and exista_simbol_start_in_dreapta:
                return False
            if este_liniara_la_dreapta is False:
                return False

            return True

    def scrie_gramatica_in_fisier(self):
        """
        Genereaza un fisier json pentru gramatica
        :return:
        """
        d = {
            "non_terminale": self.__non_terminale,
            "terminale": self.__terminale,
            "productii": self.__productii,
            "simbol_start": self.__simbol_start
        }
        json_obj = json.dumps(d)
        with open("gramatica_generata.json", "w") as outfile:
            outfile.write(json_obj)