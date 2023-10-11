import re
from BinaryTree import BinarySearchTree


def read_program():
    with open('input') as f:
        text = f.read()
    return text


def get_lexic_elements():
    """
    Stocheaza elementele lexicului(operatori, separatori, cuvinte-cheie, coduri) si le returneaza
    :return:
    """
    operatori = ['+', '-', '*', '=', '/', '==', '<', '<=', '>=', '>', '%', '<>']
    separatori = ['[', ']', '(', ')', '{', '}', ':', ';']
    cuvinte_cheie = ['then', 'for', 'while', 'const', 'string', 'integer', 'char', 'boolean', 'hello', 'bye', 'read',
                     'write', 'list', 'of', 'do', 'GO', 'DONE', 'if', 'else']
    coduri = {'identificator': 0, "constanta": 1, "+": 2, "-": 3, "*": 4, "/": 5, "=": 6, "==": 7, "<": 8, ">": 9,
              "<=": 10,
              ">=": 11, "<>": 12, "%": 13, "[": 14, "]": 15, "(": 16, ")": 17, "{": 18, "}": 19, ":": 20, ";": 21,
              ",": 22,
              '"': 23, "if": 24, "else":25, "then": 26, "for": 27, "while": 28, "const": 29, "string": 30, "integer": 31,
              "char": 32,
              "boolean": 33, "hello": 34, "bye": 35, "read": 36, "write": 37, "list": 38,
              "of": 39, "do": 40, "GO": 41, "DONE": 42}
    return operatori, separatori, cuvinte_cheie, coduri


def get_tokens():
    """
    Imparte stringul primit in tokens folosind regex, considerand ca delimitatori lista de operatori, separatori si new line, space
    :return: o lista cu tokens
    """
    #program_string = 'hello numar:integer; ? rest:integer; resu?lt:string;GO read(numar); rest=numar%3 if rest==0 then {result="multiplu3"} else{#result="nuEsteMultiplu_3"} write(result); DONE bye'
    program_string = read_program()
    pattern = '(\+|\-|\*|=|/|==|<|<=|>=|>|%|<>|\[|\]|\(|\)|\{|\}|:|;|\n|\s)'
    tokens = re.split(pattern, program_string)
    final_tokens = [token for token in tokens if token != '' and token != ' ' and token != '\n']
    return final_tokens


def check_identificator(token):
    """
    Verifica daca un token respecta lexicul unui identificator(sa inceapa cu litera si poate contine litere, cifre si caracterul '_' amestecate
    :param token: Tokenul de verificat
    :return: True daca tokenul este un identificator valid, False altfel
    """
    result = re.search('[A-Za-z]+\w*', token)
    if result is not None:
        start = result.span()[0]
        end = result.span()[1]
        if start == 0 and end == len(token):
            return True
    return False


def check_constanta(token):
    """
    Verifica daca un token este o constanta valida
    Constanta poate fi de tip intreg, string sau caracter
    :param token: tokenul de verificat
    :return: True daca tokenul este o constanta valida, False altfel
    """

    result = re.search('^[0-9]$|^\'[0-9]\'$|^[1-9]+[0-9]*$|^\"[1-9]+[0-9]+\"$|^\'[A-Za-z]\'$|^\"[A-Za-z]+\w*\"$', token)
    if result is not None:
        start = result.span()[0]
        end = result.span()[1]
        if start == 0 and end == len(token):
            return True
    return False


def get_pozitie_TS(token, TS):
    """
    Returneaza pozitia din TS a tokenului, TS-ul parcurgandu-se in inordine (left-root-right)
    :param token: tokenul pentru care se cauta pozitia
    :return: pozitia
    """
    values = []
    values = TS.inorder_traversal(values)
    return len(values), values.index(token)


def updateFIP(FIPview, nr_elem, added_position, token):
    """
    Face update la FIP, actualizand pozitia din TS corespunzatoare atomului
    :param FIPview: tabela FIP
    :param nr_elem: numarul de elemente din TSQ
    :param added_position: pozitia pe care urmeaza sa fie introdus urmatorul atom in TS
    :param token: atomul de introdus in TS
    :return: None
    """
    if nr_elem < added_position:
        return 
    for elem in FIPview:
        if elem[1] != -1 and added_position <= elem[1]:
            if elem[2] == token:
                break
            elem[1] += 1


def throw_error(token):
    """
    Afiseaza o eroare daca tokenul nu este valid
    :param token: tokenul care a fost verificat
    """
    print(f"Eroare lexicala. Atomul {token} nu este valid")


def classify_token(tokens):
    """
    Clasifica fiecare token in operator, separator, cuvant-cheie, identificator sau constanta si adauga in FIP o intrare de forma (cod_token, pozitie_in_TS),
    respectiv adauga in TS daca este cazul(pt identificatori si constante) o intrare care sa contina constanta/identificatorul si pozitia acestuia
    :param tokens: lista de tokens identificati
    :return: FIP SI TS
    """
    FIPview = []
    TS = BinarySearchTree()
    operatori, separatori, cuvinte_cheie, coduri = get_lexic_elements()
    for i, token in enumerate(tokens):
        if token in operatori or token in separatori or token in cuvinte_cheie:
            FIPview.append([coduri.get(token), -1, token])

        elif check_constanta(token):
            if TS.search(token) is False:
                TS.add_node(token)
            nr_elem, pos = get_pozitie_TS(token, TS)
            if len(FIPview) > 1:
                updateFIP(FIPview, nr_elem, pos, token)
            FIPview.append([1, pos, token])

        elif check_identificator(token):
            if TS.search(token) is False:
                TS.add_node(token)
            nr_elem, pos = get_pozitie_TS(token, TS)
            if len(FIPview) > 1:
                updateFIP(FIPview, nr_elem, pos, token)
            FIPview.append([0, pos, token])

        else:
            throw_error(token)
    return FIPview, TS


def analyse():
    tokens = get_tokens()
    print(f'Atomii identificati sunt: \n {tokens} \n')
    FIP, TS = classify_token(tokens)
    print("\n--------------------------------FIP--------------------------------------")
    print('Cod atom            |     Pozitie TS           ')
    for elem in FIP:
        print(f'{elem[0]}               {elem[1]}          ')
    print("--------------------------------------------------------------------------")
    print('\n')
    print("--------------------------------TS----------------------------------------")
    print('Pozitie       |     Atom')
    TS_elems = []
    for index, elem in enumerate(TS.inorder_traversal(TS_elems)):
        print(f'{index}               {elem}')
    print("--------------------------------------------------------------------------")


if __name__ == '__main__':
    analyse()

