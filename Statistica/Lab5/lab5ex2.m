#ex2 Interval de incredere pentru medie cand dispersia este necunoscuta

X=[2.7,2.8,2.8,2.9,2.9,2.9,2.9,2.9,3.0,3.0,3.0,3.1,3.1,3.1,3.1,3.1,3.2,3.2,3.2,3.2,3.3,3.3]

n=22
alpha = 1-0.98
media_de_selectie = mean(X)
dispersia_de_selectie = var(X)
abaterea_standard = std(X)

cuantila = tinv(1-alpha/2, n-1)
m1=media_de_selectie-cuantila*abaterea_standard/sqrt(n)
m2=media_de_selectie+cuantila*abaterea_standard/sqrt(n)
