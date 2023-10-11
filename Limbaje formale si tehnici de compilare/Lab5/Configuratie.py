from enum import Enum


class Stare(Enum):
    NORMALA = 'q'
    REVENIRE = 'r'
    TERMINARE = 't'
    EROARE = 'e'


class Configuratie:
    def __init__(self, stare, pozitie_intrare, stiva_de_lucru_Alpha:list, banda_de_intrare_Beta):
        self.__stare = stare
        self.__index = pozitie_intrare
        self.__Alpha = stiva_de_lucru_Alpha
        self.__Beta = banda_de_intrare_Beta

    def get_stare(self):
        return self.__stare

    def get_index(self):
        return self.__index

    def get_Alpha(self):
        return self.__Alpha

    def get_Beta(self):
        return self.__Beta

    def set_stare(self, stare):
        self.__stare = stare

    def set_index(self, pozitie_intrare):
        self.__index = pozitie_intrare

    def set_Alpha(self, stiva_de_lucru):
        self.__Alpha = stiva_de_lucru

    def set_Beta(self, banda_de_intrare):
        self.__Beta = banda_de_intrare

    def push_Alpha(self, elem, index=None):
        if index is None:
            self.__Alpha.append(elem)
        else:
            self.__Alpha.insert(index, elem)

    def push_Beta(self, elem):
        self.__Beta = elem + self.__Beta

    def pop_Alpha(self, index):
        self.__Alpha.pop(index)

    def pop_Beta(self):
        self.__Beta = self.__Beta[1:]

    def pop_Beta_more(self, nr):
        self.__Beta = self.__Beta[nr:]
