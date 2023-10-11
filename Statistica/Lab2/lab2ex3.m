#ex3

#n=number of trials
#p=probability of success

n=input("Dati n(numarul de incercari): ")
p=input("Dati p(probabilitatea de succes): ")

hold

x=0:n;
y=pdf('binomial',x,n,p);
plot(x,y,'r.')


y2=cdf('binomial',x,n,p);
#plot(x,y2,'b.')


stairs(x,y2) 