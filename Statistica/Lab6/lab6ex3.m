%ex 3

disp("Metoda 1\n");
disp("H0: sigma=0.4");
disp("H1: sigma!=0.4\n");

X=[6.16, 6.55, 5.32, 6.26, 6.10, 5.61, 5.87, 6.10, 6.83, 7.07, 5.60, 6.91, 6.22, 5.98, 6.21, 5.94, 5.96, 6.45];
alpha=0.05;
n=18;
sigma=std(X);

%test bilateral
h1_alpha=chi2inv(alpha/2,n-1);
h2_alpha=chi2inv(1-alpha/2,n-1);
U=[-inf, h1_alpha, h2_alpha, inf]
s=var(X);
v0=((n-1)*s*s)/(sigma^2)
if v0<h1_alpha & v0> h2_alpha
  disp("Se respinge H0, se accepta H1");
  disp("sigma != 0.4.");
else
  disp("Se accepta H0");
  disp("Este adevarat ca sigma=0.4.");
endif

%metoda 2
%disp("Metoda 2\n");
%[H,P,ci,stats]=ttest(X,m0,'alpha',alpha,'tail','right');
%if H==1
%  disp('Se respinge H0');
%    else
%    disp('Se accepta H0');
%endif
