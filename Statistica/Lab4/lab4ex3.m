#ex2 lab4

X=[20,20,21,22,22,22,23,23,23,23,23,23,24,24,24,24,24,25,25,25,25,25,25,25,25,25,26,26,27,27]
Y=[75,75,75,76,76,77,77,78,78,78,78,78,79,79,79,79,79,79,79,79,80,80,80,80,80,80,80,80,81,82]
#a)mediile
mX = mean(X)
mY = mean(Y)
#b)dispersiile
vX = var(X)
vY = var(Y)
#c)covarianta
covar = cov(X,Y)
#d) coeficientul de corelatie
coef = corrcoef(X,Y)
#e)sa se reprezinte pe acelasi grafic norul de puncte si dreapta de regresie
P = polyfit(X,Y,1)
plot(X,Y,'or')
hold on
z=0:1:40;
plot(z, polyval(P, z))
#f) sa se prognozeze valoarea lui y pentru x =2.5 si x =3.
val1 = polyval(P, 2.5)
val2 = polyval(P, 3)