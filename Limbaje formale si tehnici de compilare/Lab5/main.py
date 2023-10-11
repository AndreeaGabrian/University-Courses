import json
from Gramatica import Gramatica
from ASDR import ASDR


def meniu():
    print("------------------------------------------------")
    print("1.Citeste gramatica")
    print("2.Afiseaza gramatica")
    print("3.Verifica daca gramatica este GIC")
    print("4.Verifica daca se poate aplica ASDR")
    print("5.Transforma in recursiva dreapta")
    print("6.ASDR")
    print("x.Exit")


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


def verifica_posibilitate_aplicare_ASDR(gramatica: Gramatica):
    """
    Verifica daca se poate aplica ASDR pe gramatica
    :param gramatica: Gramatica de verificat
    :return: True daca se poate, False altfel
    """
    if gramatica.verificare_GIC() is True:
        if gramatica.verifica_gramatica_recursiva_stanga() is False:
            return True
        else:
            print("Gramatica este recursiva la stanga")
    else:
        print("Gramatica nu este independenta de context")
    return False


if __name__ == '__main__':
    gramatica = Gramatica([], [], {}, None)
    while True:
        meniu()
        optiune = input("Optiune: ")
        match optiune:
            case '1':
                filename = input("Dati numele fisierului de configurare dorit: ")
                gramatica = citeste_gramatica(filename)
            case '2':
                afiseaza_gramatica(gramatica)
            case '3':
                print(gramatica.verificare_GIC())
            case '4':
                print("Aplicare ASDR: ", verifica_posibilitate_aplicare_ASDR(gramatica))
            case '5':
                productii_transformate, non_terminale_noi = gramatica.transforma_in_recursiva_dreapta()
                gramatica.set_productii(productii_transformate)
                gramatica.set_non_terminale(non_terminale_noi)
            case '6':
                valid, prod = ASDR.algoritm_ASDR(gramatica, 'abba')
                #valid, prod = ASDR.algoritm_ASDR(gramatica, 'bb')
                print(valid)
                print(prod)
            case 'x':
                break
            case other:
                print("Mai incearca")
