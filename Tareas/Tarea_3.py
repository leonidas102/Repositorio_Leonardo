print('Seleccione una funcion:  \n' \
      '1. vocal\n2.parqueadero\n3.triangulo')
elec=input('seleccione una funcion ')
if(elec.lower()=='vocal' or elec=='1'):
    l=str(input('ingrese una letra '))
    if(l in ['a','e','i','o','u','A','E','I','O','U']):
        print('ingreso una vocal ')
    else:
        print('ingreso una consonante ')    
elif(elec.lower()=='parqueadero' or elec=='2'):
    t=int(input('ingrese la cantidad de minutos que va a usar el parqueadero '))
    m=139
    costo=m*t
    v=costo%50
    if(v==0):
        iva=costo*0.19
        base=costo-iva
        print('El valor es',base,'\n'\
              'iva= ',iva,'\n'\
                'total = ',costo)
    else:
        r=costo+v
        iva=r*0.19
        base=r-iva
        print('El valor es',base,'\n'\
              'iva= ',iva,'\n'\
                'total = ',r)
        

elif(elec.lower()=='triangulo' or elec=='3'):
    a=float(input('ingrese el primer lado del triangulo  '))
    b=float(input('ingrese el segundo lado del triangulo  '))
    c=float(input('ingrese el tercer lado del triangulo  '))
    if (a+b>c or b+c>a or a+c>b):
        if(a==b==c):
            print( 'El triangulo es equilatero')
        elif(a==b or a==c or b==c):
            print('El triangulo es isosceles')
        else:
            print('el triangulo es escaleno')   
    else:
        print('Ingrese Cantidades validas ')         
else:
    print('seleccione una funcion valida')