%ex2

X1 = [4.95 5.24 5.13 5.07 4.83 5.04 4.92 5.06 5.15 5.23 5.16 5.28];
X2 = [5.32 5.13 5.41 5.13 4.92 4.83 5.68 5.56 5.72 4.83];

%a) 

% H0:(?1)^2=(?2)^2   cu alternativa
% H1:(?1)^2=(?2)^2  test F bilateral
alpha = 0.02;
m1 = mean(X1);
m2 = mean(X2);
v1 = var(X1);
v2 = var(X2);
n1 = length(X1);
n2 = length(X2);

fprintf('\npunctul a)\n')

f1 = finv(alpha/2, n1-1, n2 -1);
f2 = finv(1-alpha/2, n1-1, n2 -1);  %test F bilateral
fprintf('Regiunea U de respingere este: (-inf, %.2f] U [%.2f, +inf)\n',f1,f2);

f0 = v1/v2;
fprintf('f0 = %.2f\n',f0);

if (f0 > -inf && f0<=f1) || (f0>=f2 && f0 < +inf) 
   fprintf('Ipoteza H0 se respinge\n')
else
   fprintf('Ipoteza H0 se accepta\n')
end

%b)
fprintf('\npunctul b)\n')
% H0:m1=m2 cu alternativa
% H1:m1<m2 test T la stanga.

sp = sqrt(((n1-1)*v1 + (n2-1)*v2)/(n1+n2-2));  %este abaterea standard de selectie combinata
t_alpha = tinv(alpha, n1+n2-2)
fprintf('Regiunea U de respingere este: (-inf, %.2f]\n',t_alpha);
t0 = (m1-m2)/(sp*sqrt(1/n1+1/n2));
fprintf('t0 = %.2f\n',t0);

if (t0 > -inf && t0<=t_alpha) 
   fprintf('Ipoteza H0 se respinge\n')
else
   fprintf('Ipoteza H0 se accepta\n')
end