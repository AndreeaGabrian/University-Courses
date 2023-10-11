from Gramatica import Gramatica
from TADAutomat import TADAutomat

EPSILON = "epsilon"


class Convertor:
    def __init__(self):
        pass

    @staticmethod
    def convert_GR_AF(gramatica: Gramatica):
        """
        Transforma o gramatica regulara in automat finit
        :param gramatica: gramatica regulara
        :return: automatul finit corespunzator
        """
        if gramatica.verifica_daca_este_regulara() is False:
            return None

        multime_stari = gramatica.get_non_terminale()
        multime_stari.append("k")
        stare_initiala = gramatica.get_simbol_start()
        alfabet = gramatica.get_terminale()

        stari_finale = ["k"]
        productii_gramatica = gramatica.get_productii()
        if EPSILON in productii_gramatica.get(stare_initiala):
            stari_finale.append(stare_initiala)

        tranzitii = []
        for (key, values) in productii_gramatica.items():
            for val in values:
                if len(val) == 1:
                    tranzitie = [key, [val], "k"]
                else:
                    tranzitie = [key, [val[0]], val[1]]
                tranzitii.append(tranzitie)

        TAD = TADAutomat(stare_initiala, multime_stari, alfabet, tranzitii, stari_finale)
        return TAD

    @staticmethod
    def convert_AF_GR(TAD: TADAutomat):
        """
        Transforma un automat finit in gramatica regulara. !!!Daca Starea initiala e si finala starting simbol merge in epsilon!!!
        :param TAD: automatul finit
        :return: gramatica regulara
        """
        simbol_start = TAD.get_stare_initiala().upper()
        non_terminale = [x.upper() for x in TAD.get_stari()]
        terminale = TAD.get_alfabet()
        tranzitii = TAD.get_tranzitii()
        stari_finale = TAD.get_stari_finale()
        productii = {}
        for nt in non_terminale:
            productii[nt] = []
        for tranzitie in tranzitii:
            stare_stanga = tranzitie[0].upper()
            stare_dreapta = tranzitie[2].upper()
            terminale_stare = tranzitie[1]
            for ter in terminale_stare:
                productii[stare_stanga].append(ter+stare_dreapta)
                if stare_dreapta.lower() in stari_finale:
                    productii[stare_stanga].append(ter)

        stari_finale_fara_tranzitii = []
        for (key, value) in productii.items():
            if len(value) == 0:
                stari_finale_fara_tranzitii.append(key)
        for key in stari_finale_fara_tranzitii:
            del productii[key]

        gramatica = Gramatica(non_terminale, terminale, productii, simbol_start)
        return gramatica


