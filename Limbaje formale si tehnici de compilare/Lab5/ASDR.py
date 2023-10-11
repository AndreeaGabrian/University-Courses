from Configuratie import Configuratie, Stare
from Gramatica import Gramatica
EPSILON = "epsilon"


def print_step(configuratie):
    step = (configuratie.get_stare(), configuratie.get_index(), configuratie.get_Alpha(), configuratie.get_Beta())
    print(step)


class ASDR:
    def __init__(self):
        pass

    @staticmethod
    def algoritm_ASDR(gramatica, secventa):

        #configuratie = Configuratie(Stare.NORMALA, 1, [EPSILON], gramatica.get_simbol_start())     # s:=q; i:=1; α:=ε; β:=S; //config initiala
        configuratie = Configuratie(Stare.NORMALA, 1, [], gramatica.get_simbol_start())     # s:=q; i:=1; α:=ε; β:=S; //config initiala
        print_step(configuratie)
        while configuratie.get_stare() != Stare.TERMINARE and configuratie.get_stare() != Stare.EROARE:      # Cattimp ((s≠t) si (s ≠e)) executa
            if configuratie.get_stare() == Stare.NORMALA:     # daca (s=q) atunci
                if len(configuratie.get_Beta()) == 0 and configuratie.get_index() == len(secventa)+1:   # daca ((β=ε) si (i=n+1)) atunci
                    configuratie.set_stare(Stare.TERMINARE)    # s:=t

                else:
                    if len(configuratie.get_Beta()) != 0:
                        varf_beta = configuratie.get_Beta()[0]   # varf(β)
                        if varf_beta in gramatica.get_non_terminale():     # daca (varf(β) = A) atunci         expandare
                            print("expandare")
                            prima_productie_dreapta_varf_Beta = gramatica.get_productii_pentru_simbol(varf_beta)[0]   #ϒ
                            configuratie.push_Alpha((varf_beta, prima_productie_dreapta_varf_Beta))   # push(α, A1);
                            configuratie.pop_Beta()    # pop(β, A1);
                            configuratie.push_Beta(prima_productie_dreapta_varf_Beta)   # push(β, ϒ);

                            print_step(configuratie)

                        else:
                            i = configuratie.get_index()
                            print("avans, ",secventa, ", ",i)

                            if i <= len(secventa):
                                if varf_beta == secventa[i-1]:    # daca (varf (β) = xi) atunci        //avans
                                    configuratie.set_index(i + 1)       # i:=i+1;
                                    configuratie.push_Alpha(varf_beta)   # push(α, a);
                                    configuratie.pop_Beta()    # pop(β,a)

                                    print_step(configuratie)

                                else:
                                    configuratie.set_stare(Stare.REVENIRE)      # s:=r;  //insucces de moment
                                    print_step(configuratie)
                            else:
                                #configuratie.set_stare(Stare.REVENIRE)
                                configuratie.set_stare(Stare.EROARE)
                    else:
                        configuratie.set_stare(Stare.REVENIRE)
                        print_step(configuratie)

            elif configuratie.get_stare() == Stare.REVENIRE:       # daca(s=r) atunci   // daca sunt in r pot face revenire sau alts incercare
                print("stare=revenire")
                print_step(configuratie)
                if len(configuratie.get_Alpha()) != 0:     #daca Alpha nu e gol
                    varf_alpha = configuratie.get_Alpha()[-1]

                    if varf_alpha[0] in gramatica.get_terminale():      # daca (varf(α)=a) atunci
                        i = configuratie.get_index()
                        configuratie.set_index(i - 1)        # i:=i-1;
                        configuratie.pop_Alpha(-1)    # pop(α,a);
                        configuratie.push_Beta(varf_alpha[0])     # push (β,a);

                        print_step(configuratie)
                    else:
                        prev_prod = configuratie.get_Alpha()[-1]
                        print("prev prod: ", prev_prod)
                        prev_prod_dreapta = gramatica.get_productii_pentru_simbol(prev_prod[0])   # prev_prod_dreapta este o lista cu toate productiile din partea dreapta a unui simbol
                        print("prev prod dreapta: ",prev_prod_dreapta)
                        index_next_prod_dreapta = prev_prod_dreapta.index(prev_prod[1]) + 1
                        if index_next_prod_dreapta <= len(prev_prod_dreapta) - 1:          # daca (ⱻ A→ ϒj+1 si A→ ϒj a fost ultima folosita ) atunci
                            next_prod_dreapta = prev_prod_dreapta[index_next_prod_dreapta]
                            configuratie.set_stare(Stare.NORMALA)    # s:=q;   //alta incercare1

                            print(configuratie.get_Beta(), configuratie.get_Alpha())
                            configuratie.pop_Alpha(-1)  # pop(α, Aj)
                            print(configuratie.get_Beta(), configuratie.get_Alpha())
                            configuratie.push_Alpha((prev_prod[0], next_prod_dreapta))  # push(α, Aj+1);
                            #scot toata productia din beta
                            #configuratie.pop_Beta()  # pop(β, ϒj);
                            configuratie.pop_Beta_more(len(prev_prod[1]))

                            configuratie.push_Beta(next_prod_dreapta)  # push (β, ϒj+1,);

                            print_step(configuratie)
                        else:
                            if configuratie.get_index() == 1 and prev_prod[0] == gramatica.get_simbol_start:   # daca (i=1) si (A=S) atunci
                                configuratie.set_stare(Stare.EROARE)   # s:=e;      //alta incercare 3
                                print_step(configuratie)
                            else:
                                configuratie.pop_Alpha(-1)  # pop(α, Aj)          //alta incercare 2
                                configuratie.push_Beta((prev_prod[0], prev_prod[1]))  # push(β, Aj);

                                print_step(configuratie)
                else:
                    configuratie.set_stare(Stare.EROARE)
                    print_step(configuratie)

        sir_productii = []
        if configuratie.get_stare() == Stare.EROARE:
            print("Eroare, secventa nu e acceptata")
            return False, []
        else:
            for elem in configuratie.get_Alpha():
                if len(elem) == 2:
                    sir_productii.append(elem)
        return True, sir_productii












