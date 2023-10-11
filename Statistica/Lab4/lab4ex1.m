#ex1 lab4

X=[-2,-1,0,1,2]
Y=[0,0,1,1,3]
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
xlim=([0 100])
plot(X,Y,'or')
hold on
z=-10:1:10;
plot(z, polyval(P, z))
#f) sa se prognozeze valoarea lui y pentru x=2.5 si x=3.
val1 = polyval(P, 2.5)
val2 = polyval(P, 3)