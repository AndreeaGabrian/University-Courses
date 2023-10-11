%ex 1

disp("Metoda 1\n");
disp("H0: m=3.6");
disp("H1: m<3.6\n");

X=[3.5,3.3,3.6,3.2,3.4,3.1,3.5,3.7,3.3];
m0=3.6;
alpha=0.04; %nivelul de semnificatie, probabilitate de risc
sigma=0.18; %abaterea standard
%test Z la stanga
z_alpha=norminv(alpha,0,1);
U=[-inf,z_alpha]
n=length(X);
z0=(mean(X)-m0)/(sigma/sqrt(n))
if z0<z_alpha
  disp("Se respinge H0, se accepta H1");
  disp("Laptele nu respecta normele calitative.");
else
  disp("Se accepta ip nula H0");
  disp("Laptele respecta normele calitative");
endif

%metoda 2
%disp("Metoda 2\n");
%[H,PVAL,CI,Z,ZCRIT]=ztest(X,m0,sigma,'alpha',alpha,'tail','left');
%if H==1
%  disp('se respinge H0');
%else
%  disp('se accpeta H0');
%endif
