import json

from Convertor import Convertor
from Gramatica import Gramatica
from TADAutomat import TADAutomat


def meniu():
    print("------------------------------------------------")
    print("1.Citeste gramatica")
    print("2.Afiseaza gramatica")
    print("2a.Afiseaza productiile pentru un non-terminal dat")
    print("3.Verifica daca gramatica este regulara")
    print("4.Conversie GR->AF")
    print("5.Conversie AF->GR")
    print("x.Exit")


def meniu2():
    print("\n------------------------------------------------")
    print("1.AF Constante")
    print("2.AF Identificatori")
    print("x.Exit")


def meniu3():
    print("\n -----------------------------------------------")
    print("1.Multimea starilor")
    print("2.Alfabet")
    print("3.Tranzitii")
    print("4.Starile finale")
    print("5.Starea initiala")
    print("6.Verifica secventa")
    print("7.Returneaza stare pentru simbol si stare date")
    print("8.Conversie in gramatica regulara")
    print("x.Exit")


def load_config(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    TAD = TADAutomat(data["stare_initiala"], data["stari"], data["alfabet"], data["tranzitii"], data["stari_finale"])
    return TAD


def citeste_gramatica(filename):
    try:
        with open(filename,'r') as f:
            data = json.load(f)
        gramatica = Gramatica(data["non_terminale"], data["terminale"],data["productii"],data["simbol_start"])
        print("Gramatica a fost citita\n")
        return gramatica
    except:
        print("Eroare la citirea gramaticii din fisier\n")
        return None


def afiseaza_gramatica(gramatica: Gramatica):
    s = ", "
    non_terminale = s.join(gramatica.get_non_terminale())
    terminale = s.join(gramatica.get_terminale())
    print("Non-terminale: {}".format(non_terminale))
    print("Terminale: {}".format(terminale))
    print("Productii: ")
    productii = gramatica.get_productii()
    for (key, values) in productii.items():
        print("{} -> {}".format(key, '|'.join(values)))
    print("Simbol de start: {}".format(gramatica.get_simbol_start()))


def afiseaza_productii_non_terminal(gramatica:Gramatica, non_terminal):
    if non_terminal in gramatica.get_non_terminale():
        productii = gramatica.get_productii().get(non_terminal)
        print("Productiile pentru {} sunt: ".format(non_terminal))
        print("{} -> {}".format(non_terminal, "|".join(productii)))
    else:
        print("Non-terminalul dat nu se afla in gramatica")


if __name__ == '__main__':
    gramatica = Gramatica([], [], {}, None)
    while True:
        meniu()
        optiune = input("Optiune: ")
        match optiune:
            case '1':
                filename = input("Dati numele fisierului de configurare dorit: ")
                gramatica = citeste_gramatica("config.json")
                #gramatica = citeste_gramatica(filename)
            case '2':
                afiseaza_gramatica(gramatica)
            case '2a':
                non_terminal = input("Dati non-terminalul: ")
                afiseaza_productii_non_terminal(gramatica, non_terminal)
            case '3':
                if gramatica.verifica_daca_este_regulara():
                    print("Gramatica este regulara\n")
                else:
                    print("Gramatica nu este regulara\n")
            case '4':
                TAD = Convertor.convert_GR_AF(gramatica)
                if TAD is not None:
                    print("Automatul este: ")
                    print("Stari: ", TAD.get_stari())
                    print("Alfabet: ", TAD.get_alfabet())
                    print("Tranzitii: ", TAD.get_tranzitii())
                    print("Stari finale: ", TAD.get_stari_finale())
                    print("Stare initiala: ", TAD.get_stare_initiala())
                    TAD.scrie_tad_in_fisier()
                else:
                    print("Gramatica nu este regulara, nu se poate face conversia")
            case '5':
                while True:
                    meniu2()
                    TAD = ''
                    optiune = input("Optiune: ")
                    if optiune == '1':
                        TAD = load_config("constante.json")
                    if optiune == '2':
                        TAD = load_config("identificatori.json")
                    ok = True
                    while ok:
                        meniu3()
                        optiune = input("Optiune: ")
                        match optiune:
                            case '1':
                                print(TAD.get_stari())
                            case '2':
                                print(TAD.get_alfabet())
                            case '3':
                                print(TAD.get_tranzitii())
                            case '4':
                                print(TAD.get_stari_finale())
                            case '5':
                                print(TAD.get_stare_initiala())
                            case '6':
                                secventa = input("Dati secventa: ")
                                if TAD.verifica_secventa(secventa):
                                    print("Secventa acceptata")
                                else:
                                    print("Secventa respinsa")
                            case '7':
                                stare = input("Dati starea: ")
                                simbol = input("Dati simbolul: ")
                                end = TAD.get_stare_pentru_simbol(stare, simbol)
                                if end is not None:
                                    print(end)
                                else:
                                    print("Nu exista tranzitie pentru starea si simbolul dat")
                            case '8':
                                gramatica_AF = Convertor.convert_AF_GR(TAD)
                                afiseaza_gramatica(gramatica_AF)
                                gramatica_AF.scrie_gramatica_in_fisier()
                            case 'x':
                                break
                            case other:
                                print("Mai incearca!")
            case 'x':
                break
            case other:
                print("Mai incearca!\n")