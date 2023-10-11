#ex1 Interval de ?ncredere pentru medie and dispersia este cunoscuta

X=[22.7,22.8,22.8,22.8,22.9,22.9,22.9,22.9,22.9,22.9,22.9,23.0,23.0,23.0,23.0,23.1,23.1,23.1,23.1,23.1,23.1,23.2,23.2,23.2,23.2,23.2,23.2,23.2,23.3,23.3,23.3,23.3,23.3,23.4,23.4]
var_X = 0.35
alpha = 1-0.95

media_de_selectie = mean(X)
dispersia_de_selectie = var(X)
abaterea_standard = std(X)
dispersia_teoretica = 0.35

cuantila = norminv(1-alpha/2,0,1)
m1 = media_de_selectie - cuantila * sqrt(dispersia_teoretica)/sqrt(35)
m2 = media_de_selectie + cuantila * sqrt(dispersia_teoretica)/sqrt(35)
