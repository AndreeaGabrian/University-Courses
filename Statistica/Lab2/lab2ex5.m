n=input("Dati n: ")

[m,v] = tstat(n);
sigma = sqrt(v);

x=m-3*sigma:0.01:m+3*sigma;
y1=tpdf(x,n);

hold on
plot(x,y1,'b')

y2=tcdf(x,n);
plot(x,y2,'r')