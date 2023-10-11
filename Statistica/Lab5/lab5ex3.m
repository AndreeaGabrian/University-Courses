#ex3 Interval de increddere pentru dispersia legii normale

X=[4.21,4.03,3.99,4.05,3.89,3.98,4.01,3.92,4.23,3.85,4.20]
n=11
prob_de_incredere = 0.95
alpha = 1-0.95
dispersia_de_selectie = var(X)

cuantila_alpha_supra2 = chi2inv(alpha/2,n-1)
cuantila_1minus_alpha_supra2 = chi2inv(1-alpha/2,n-1)

#intevalul de incredere pentru dispersia teoretica sigma^2
d1 = (n-1)*dispersia_de_selectie/cuantila_1minus_alpha_supra2
d2 = (n-1)*dispersia_de_selectie/cuantila_alpha_supra2

#intervalul de incredere pentru abaterea standard sigma 
D1 = sqrt((n-1)*dispersia_de_selectie/cuantila_1minus_alpha_supra2)
D2 = sqrt((n-1)*dispersia_de_selectie/cuantila_alpha_supra2)