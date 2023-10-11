N=input("Dati N: ")
a=input("Dati a: ")
sibgma=input("Dati b: ")

#generam random N date(numere) care respecta legea normala de parametri miu si sigma
X=random('uniform', a, b, [1,N]);
#ordonam crescatorul sirul de N numere generat
X_sorted = sort(X)
#calculam minimul si maximul sirului
X_min=min(X_sorted)
X_max=max(X_sorted)

#n este numarul de clase, vrem sa determinam numarul de clase disjuncte(cu regula lui Sturges)
n=floor(1+10/3*log10(N))
#calculam d(lungimea claselor)
d=(X_max-X_min)/n
#vectorul clase va contine extremitatile claselor(capetele intervalelor)

clase = [];
for i=1:n+1 
  ci = X_min + (i-1)*d;
  clase=[clase, ci];
endfor


#determinam frecventele absolute ale claselor f(=nr de date primare care se gasesc in clasa i) si mijloacele claselor
#folosimpt asta fct hist care returneaza  numarul de elemente(bars) si mijloacele lor
[fi, middle] = hist(X,n);

#Afisam tabelul statistic sistematizat

disp_nr=["Nr."];
disp_clase = ["        Clasa"];
disp_fi=["   Frecventa absoluta"];
disp_middle=["       Mijlocul clasei"];
disp_frel=["Frecventa relativa"];
for i=1:n
  disp_nr = [disp_nr;mat2str(i)];
  disp_clase = [disp_clase;"        [",mat2str(clase(i)),", ", mat2str(clase(i+1)), ")          "];
  disp_fi = [disp_fi;"       ",mat2str(fi(i)),"      "];
  disp_middle=[disp_middle;"      ", mat2str(middle(i)),"      "];
  disp_frel = [disp_frel;mat2str(fi(i)/N)];
endfor
disp_nr 
disp_clase 
disp_fi 
disp_middle 
disp_frel

table = [disp_nr disp_clase disp_fi disp_middle disp_frel]

#reprezentare grafica a histogramei frecventelor absolute
hist(X,n)
hold on;
#poligonul frecventelor absolute
plot(middle,fi,'o-g')

#media aritmetica, geometrica, armonica
arithmetic_mean = mean(X);
fprintf("Media aritmetica este: %d \n",arithmetic_mean)
geometric_mean = geomean(X);
fprintf("Media geometrica este: %d \n",geometric_mean)
harmonic_mean = harmmean(X);
fprintf("Media armonica este: %d \n",harmonic_mean)
#mediana = valoarea care imparte datele statistice ordonate crescator in doua parti egale
X_median = median(X_sorted) 

#calculam modul(mod= orice punct de maxim local al distributiei statistice X(middle1 ... middlen))
#                                                                              f1    ...    fn
i=find(fi==max(fi));
mod = middle(i);
fprintf("Modul este: %d \n",mod)

#calculam cuartilele
fprintf("CUartilele sunt: /n")
Q=prctile(X_sorted)
#dispersia si abaterea standard 
dispersie=var(X);
fprintf("Dispersia este: %d \n",dispersie)
abatere_standard=std(X);
fprintf("Abaterea standard este: %d \n",abatere_standard)

#calculam momentele centrate de ordin 1,2,3,4
m1=moment(X,1);
m2=moment(X,2);
m3=moment(X,3);
m4=moment(X,4);

format short 
fprintf("Momentul de ordin 1: %d \n",m1)
fprintf("Momentul de ordin 2: %d \n",m2)
fprintf("Momentul de ordin 3: %d \n",m3)
fprintf("Momentul de ordin 4: %d \n",m4)