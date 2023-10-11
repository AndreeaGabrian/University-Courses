#ex11
format short
a=4/3
format long 
a=4/3

#ex 12
a=1;b=2;c=3;
fprintf('a = %d , b = %d , c = %d \n', a, b, c);
fprintf('a=%d b=%d ', a, b); fprintf('a+b=%d \n ', a+b);
a = 3.7; b = 4;
fprintf('a=%2.3f , b=%8d \n', a, b);
fprintf('Suma este = %2.5f \n', a+b);
x = 0:0.2:1;
disp(x)
fprintf('%2.3f ',x); fprintf('\n');
fprintf('%2.3f \n',x);
a=[x; 5*x];
disp(a)
fprintf('%4.2f %10.6f\n',a);