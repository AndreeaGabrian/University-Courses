m=input("Dati m: ")
sigma=input("Dati sigma: ")

x=m-3*sigma:0.01:m+3*sigma;
y1=normpdf(x,m,sigma);

hold
plot(x,y1,'b')

y2=normcdf(x,m,sigma);
plot(x,y2,'r')