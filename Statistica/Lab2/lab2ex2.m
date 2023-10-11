#ex2

#p1=0.3;
#p2=0.4;

x=0:16;
p=input("Dati p: ")

hold
y1=pdf('geometric',x,p)
plot(x,y1,'r.')


y12=cdf('geometric',x,p)
#plot(x,y12,'k.')
stairs(x,y12)






#y1=pdf('geometric',x,p1)
#plot(x,y1,'r.')


#y12=cdf('geometric',x,p1)
#plot(x,y12,'k.')


#holdy2=pdf('geometric',x,p2)
#plot(x,y2,'b.')


#y22=cdf('geometric',x,p2)
#plot(x,y22,'g.')