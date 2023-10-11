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

    def get_productii_pentru_simbol(self, simbol):
        """
        Returneaza toate productiile pentru un simbol
        :param simbol: Simbolul pentru care sa se dea productiile
        :return: productiile
        """
        return self.__productii.get(simbol)

    def set_non_terminale(self, non_terminale):
        self.__non_terminale = non_terminale

    def set_terminale(self,terminale):
        self.__terminale = terminale

    def set_productii(self,productii):
        self.__productii = productii

    def set_simbol_start(self, simbol_start):
        self.__simbol_start = simbol_start

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

    def verificare_GIC(self):
        """
        O gramatica G=(N, Σ, P, S) este independenta de context daca productiile P ale gramaticii sunt numai de forma
        𝐴 → 𝛼, 𝐴 ∈ 𝑁, 𝛼 ∈ (𝑁 ∪ Σ)* (adica in partea stanga a productiei avem doar un singur non-terminal, iar in dreapta putem avea orice)
        :return: True daca gramatica este independenta de context, False altfel
        """

        for prod_stanga, prod_drepata in self.__productii.items():
            if len(prod_stanga) != 1 or prod_stanga not in self.__non_terminale:
                return False
            for one_prod in prod_drepata:
                if prod_drepata == "EPSILON":
                    continue
                for litera in one_prod:
                    if litera not in self.__terminale and litera not in self.__non_terminale:
                        return False
        return True

    def verificare_recursivitate_la_stanga_productie(self, productie_stanga, productie_dreapta):
        """
        Verifica daca o productie este recursiva la stanga. O productie este recursiva la stanga daca este de forma
        𝐴 → 𝐴𝛼
        :param productie_stanga: Partea stanga a productiei de verificat
        :param productie_dreapta: Partea dreapta a productiei de verificat
        :return: True daca este resursiva la stanga, False altfel
        """
        for elem in productie_dreapta:
            if productie_stanga == elem[0]:
                return True
        return False

    def verifica_gramatica_recursiva_stanga(self):
        """
        Verifica daca o gramatica are cel putin o productie recursiva la stanga
        :return: True daca are, False daca nu are
        """
        for (productie_stanga, productie_dreapta) in self.__productii.items():
            if self.verificare_recursivitate_la_stanga_productie(productie_stanga, productie_dreapta):
                return True
        return False

    def transforma_in_recursiva_dreapta(self):
        """
        Transforma o gramatica recursiva la stanga intr-una recursiva la dreapta
        Regula transformare:
        A->Aa | b devine:
                            A->bA'   (prod1)
                            A'->aA' | epsilon  (prod2)
        :return: Un dictionar cu toate productiile gramaticii unde cele recursive la stanga sunt transformate in recursive la dreapta
                 si o lista cu noile non terminale
        """
        productii_tranformate = {}
        non_terminale_introduse = []  #non terminalele introduse daca avem gramatica recursiva la stanga
        for (productie_stanga, productie_dreapta) in self.__productii.items():
            elem_recursive = []  # lista cu elem recursive din partea dr a unei productii
            elem_nerecursive = []  # elem nerecursive sunt orice elem nerecursive la stanga care nu sunt terminale(combinatii de terminale si non-terminale
            # ex aA, BA, aAbB, etc
            for index, elem in enumerate(productie_dreapta):  #parcurgem partea dreapta a productiei element cu element
                if productie_stanga == elem[0]:    #inseamna ca avem in dreapta un elem recursiv la stanga
                    elem_recursive.append(elem)
                else:
                    elem_nerecursive.append(elem)

            #cream noile productie dupa regula de transformare de mai sus doar daca avem recursivitate
            if len(elem_recursive) > 0:
                #construim prod1
                prod1_dreapta = []
                noul_non_terminal = productie_stanga + "'"
                for elem_nerec in elem_nerecursive:
                    prod1_dreapta.append(elem_nerec+noul_non_terminal)

                productii_tranformate[productie_stanga] = prod1_dreapta #am adaugat prod1 in dictionarul de productii

                #construim prod2
                prod2_dreapta = []
                for elem_rec in elem_recursive:
                    elem_modificat = elem_rec[1:] + noul_non_terminal
                    prod2_dreapta.append(elem_modificat)
                #adaugam epsilon in a doua productie rezultata
                prod2_dreapta.append(EPSILON)

                productii_tranformate[noul_non_terminal] = prod2_dreapta #am adaugat prod2 in dictionarul de productii
                non_terminale_introduse.append(noul_non_terminal)
            else:
                productii_tranformate[productie_stanga] = productie_dreapta #daca nu avem elem recursive in productie o adaugam neschimbata

        return productii_tranformate, self.__non_terminale + non_terminale_introduse







