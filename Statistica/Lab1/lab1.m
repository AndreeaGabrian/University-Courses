#ex1
a=[1 2;3 4;5 6]
temp=a(1,:);
a(1,:) = a(3,:);
a(3,:)=temp;
a

#ex2
a=[1 2 3; 4 5 6]
temp=a(:,2);
a(:,2)=a(:,3);
a(:,3)=temp;
a

#ex3
v=[1 2 3 4 5 6 11 13]
t=v(1,3:7)

#ex4
a=[1 2 3; 4 5 6; 7 8 9]
t=a([2:3],[1:2])

#ex5
a1=zeros(3)
a2=zeros(4, 6)
a3=eye(2, 3)
a4=ones(3)
a5=ones(3,4)
a6=magic(2)
a7=magic(4)

#ex6 se face comparatia element cu element 
u = [1 2 3]
v = [4 5 6]
u==v
u!=v
u<v
u>v
u<=v
u>=v

#ex7
t=[2*u (-3)*v]

#ex8
#syms x y z
#eq1 = 3*x + 2*y + z == 8;
#eq2 = -4*x + y + z == 6;
#eq3 = x + 4*y - 3*z == -12;
#sol = solve([eq1, eq2, eq3], [x, y, z]);
#x_sol = sol.x
#y_sol = sol.y
#z_sol = sol.z

A=[1 2 3; 4 2 -3; -2 1 3]
B=[1;2;3]
res=linsolve(A,B)

#ex9
A=[1 2 3; 4 2 -3; -2 1 3]
B=[1 2 3; 1 1 -1; -1 4 6]
rez=ex9(A,B)

#ex10
rez2=ex10(A,B)
