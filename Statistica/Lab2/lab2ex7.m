lambda=input("Dati lambda: ")

[m,v] = expstat(lambda);
sigma = sqrt(v);

x=max(0, m-3*sigma):0.01:m+3*sigma;
y1=exppdf(x,lambda);

%hold on
figure(1)
plot(x,y1,'b')

y2=expcdf(x,lambda);
figure(2)
plot(x,y2,'r')