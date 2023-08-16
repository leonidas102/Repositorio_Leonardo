import math as m

a=int(input("ingrese a "))
b=int(input("ingrese b "))
c=int(input("ingrese c "))
raiz=b**2-4*a*c
if raiz>0:
  x1=(-b+m.sqrt(b**2-4*a*a))/(2*a)
  x2=(-b-m.sqrt(b**2-4*a*a))/(2*a)
  print("solución es ",x1 , x2)
else:
  raiz=m.fabs(raiz)
  x_r=-b/2*a
  x_i=m.sqrt(raiz)/2*a
  print("el resultado es \n"\
        ,x_r, "+",x_i,"i\n"
        ,x_r, "-",x_i,"i")  