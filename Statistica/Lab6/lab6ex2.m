%ex 2

disp("Metoda 1\n");
disp("H0: m=2.55");
disp("H1: m>2.55\n");  %test T la dreapta

X=[2.51*ones(1,1),2.52*ones(1,2),2.53*ones(1,4),2.54*ones(1,5),2.55*ones(1,7),2.56*ones(1,6),2.57*ones(1,7),2.58*ones(1,2),2.59*ones(1,1),];
m0=2.55;
alpha=0.05;
n=35;
sigma=std(X);
t_alpha=tinv(1-alpha,n-1);
U=[t_alpha,inf]

t0=(mean(X)-m0)/(sigma/sqrt(n))
if t0>t_alpha
  disp("Se respinge H0, se accepta H1");
  disp("Anul viitor pretul mediu va fi mai mare fata de cel din anul curent.");
else
  disp("Se accepta H0");
  disp("Nu se sustine ipoteza ca anul viitor pretul mediu va fi mai mare fata de cel din anul curent.");
endif

%metoda 2
%disp("Metoda 2\n");
%[H,P,ci,stats]=ttest(X,m0,'alpha',alpha,'tail','right');
%if H==1
%  disp('Se respinge H0');
%    else
%    disp('Se accepta H0');
%endif
