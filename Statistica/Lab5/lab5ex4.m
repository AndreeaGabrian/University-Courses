#ex4 Interval de incredere pentru raportul dispersiilor si diferenta mediilor

X1=[1010 993 992 1008 1006 998 1008 994 996 1006 1005 1002 997 1004 1002 1010 1003]
X2=[1002 985 996 1010 1004 1003 1010 993 1002 1006 988 995]

media_de_selectie_X1 = mean(X1)
media_de_selectie_X2 = mean(X2)
dispersia_de_selectie_X1 = var(X1)
dispersia_de_selectie_X2 = var(X2)
abaterea_standard_X1 = std(X1)
abaterea_standard_X2 = std(X2)

alpha = 0.05  #alpha=probabilitatea de risc
n1=17
n2=12

#a) Sa se determine un interval de ?ncredere pentru raportul dispersiilor teoretice

cuantila_alpha_supra2 = finv(alpha/2, n1-1, n2-1)
cuantila_1minus_alpha_supra2 = finv(1-alpha/2, n1-1, n2-1)

f1 = (1/cuantila_1minus_alpha_supra2) * (dispersia_de_selectie_X1/dispersia_de_selectie_X2)
f2 = (1/cuantila_alpha_supra2) * (dispersia_de_selectie_X1/dispersia_de_selectie_X2)


#b) Presupunand ca ?1 = ?2, sa se determine un interval de ?ncredere pentru diferenta
#   mediilor teoretice m1 ? m2

#sp = abaterea standard de selectie combinata
sp = sqrt( ((n1-1)*dispersia_de_selectie_X1 + (n2-1)*dispersia_de_selectie_X2)/(n1+n2-2) )
t_1minus_alpha_supra2 = tinv(1-alpha/2, n1+n2-2)

m1_caciula = (media_de_selectie_X1-media_de_selectie_X2) - t_1minus_alpha_supra2*sp*sqrt(1/n1 + 1/n2)
m2_caciula = (media_de_selectie_X1-media_de_selectie_X2) + t_1minus_alpha_supra2*sp*sqrt(1/n1 + 1/n2)


#c) Presupunand ca ?1 != ?2, sa se determine un interval de ?ncredere pentru diferenta
#   mediilor teoretice m1 ? m2

c = (dispersia_de_selectie_X1/n1) / (dispersia_de_selectie_X1/n1 + dispersia_de_selectie_X2/n2) 
n = 1 / (c^2/(n1-1) + (1-c)^2/(n2-1))
T_1minus_alpha_supra2 = tinv(1-alpha/2, n)

m1_caciula = (media_de_selectie_X1-media_de_selectie_X2) - T_1minus_alpha_supra2*sqrt(dispersia_de_selectie_X1/n1 + dispersia_de_selectie_X2/n2)
m2_caciula = (media_de_selectie_X1-media_de_selectie_X2) + T_1minus_alpha_supra2*sqrt(dispersia_de_selectie_X1/n1 + dispersia_de_selectie_X2/n2)



