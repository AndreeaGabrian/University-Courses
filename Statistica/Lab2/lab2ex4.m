lambda=input("Dati parametrul lambda: ")
x=0:4*lambda;

hold
y=pdf('poisson',x,lambda);
plot(x,y,'r.')

y2=cdf('poisson', x, lambda);
stairs(x,y2);