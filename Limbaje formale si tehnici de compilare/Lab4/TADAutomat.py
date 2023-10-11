import json


class TADAutomat:

    def __init__(self, stare_initiala, stari: list, alfabet: list, tranzitii: list, stari_finale: list):
        self.__stare_initiala = stare_initiala
        self.__stari = stari
        self.__alfabet = alfabet
        self.__tranzitii = tranzitii
        self.__stari_finale = stari_finale

    def get_stari(self):
        return self.__stari

    def get_stare_initiala(self):
        return self.__stare_initiala

    def get_alfabet(self):
        return self.__alfabet

    def get_tranzitii(self):
        return self.__tranzitii

    def get_stari_finale(self):
        return self.__stari_finale

    def verifica_secventa(self, secventa):
        """
        Verifica daca o secventa data este acceptata de catre automat
        :param secventa: secventa primita
        :return: True daca este acceptata, False altfel
        """
        if len(secventa) == 0:
            return False
        first = secventa[0]
        stare_intermediara = self.get_stare_pentru_simbol(self.get_stare_initiala(), first)
        if stare_intermediara is None:
            return False
        for elem in secventa[1:]:
            stare_intermediara = self.get_stare_pentru_simbol(stare_intermediara, elem)
            if stare_intermediara is None:
                return False
        if stare_intermediara in self.get_stari_finale():
            return True
        return False

    def get_stare_pentru_simbol(self, stare, simbol):
        """
        Pentru o anumita stare si un simbol de pe banda de intrare returneaza starea in care se ajunge
        :param stare: starea care se da
        :param simbol:simbolul de pe banda
        :return:starea in care se ajunge sau None daca nu se ajunge nicaieri
        """
        for tranzitie in self.__tranzitii:
            if tranzitie[0] == stare and simbol in tranzitie[1]:
                return tranzitie[2]
        return None

    def scrie_tad_in_fisier(self):
        """
        Genereaza un fisier json pentru automat
        :return:
        """
        d = {
            "stare_initiala": self.__stare_initiala,
            "stari": self.__stari,
            "alfabet": self.__alfabet,
            "tranzitii": self.__tranzitii,
            "stari_finale": self.__stari_finale
        }
        json_obj = json.dumps(d)
        with open("automat_generat.json", "w") as outfile:
            outfile.write(json_obj)
