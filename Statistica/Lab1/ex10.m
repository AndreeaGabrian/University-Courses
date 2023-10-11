function rez=ex10(A,B)
  fprintf('A.*B=')
  r1=A.*B
  fprintf('A./B=')
  r2=A./B
  fprintf('A.^2=')
  r3=A.^2
  rez=[r1,r2,r3]
end