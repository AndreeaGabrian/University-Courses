from TADAutomat import TADAutomat
import json


def menu1():
    print("\n------------------------------------------------")
    print("1.Constante")
    print("2.Identificatori")
    print("x.Exit")


def menu2():
    print("\n -----------------------------------------------")
    print("1.Multimea starilor")
    print("2.Alfabet")
    print("3.Tranzitii")
    print("4.Starile finale")
    print("5.Starea initiala")
    print("6.Verifica secventa")
    print("7.Returneaza stare pentru simbol si stare date")
    print("x.Exit")


def load_config(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    TAD = TADAutomat(data["stare_initiala"], data["stari"], data["alfabet"], data["tranzitii"], data["stari_finale"])
    return TAD


if __name__ == '__main__':
    while True:
        menu1()
        TAD = ''
        optiune = input("Optiune: ")
        if optiune == '1':
            TAD = load_config("constante.json")
        if optiune == '2':
            TAD = load_config("identificatori.json")
        ok = True
        while ok:
            menu2()
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
                case 'x':
                    break
                case other:
                    print("Mai incearca!")





