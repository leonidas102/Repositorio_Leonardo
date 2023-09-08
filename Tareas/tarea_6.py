print('Seleccione el codigo a ejecutar: \n\
 1.Divisores \n 2.Producto \n 3.Fibbonacci')
O=input('Seleccione una opcion: ')

if (O=="1") or (O.lower()=="Divisores" ):
    div=int(input("Ingrese un número: "))
    if div==0:
        print("Ningún número es divisible entre cero")
    else:
        print("Los divisores positivos de",div,"son: ")
        for i in range(1,div+1):
            if div%i == 0:
                print(i)
elif (O=="2") or (O.lower()=="Producto" ):
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    p=0
    if n2<0:
        n1,n2 = -n1,-n2
    for _ in range(n2):
        p+= n1
    print("El producto entre", n1, "y", n2, "es:", p)
        
elif (O=="3") or (O.lower()=="Fibonacci" ):
    n=int(input("ingrese un numero "))
    s1=1
    s2=1
    s3=s1+s2
    print(str(s1)+","+str(s2),end=",")
    for i in range(1, n):
        i+=1
        s3=s1+s2
        s1=s2
        print(str(s3),end= ",")
        s2=s3
else:
    print('Ingrese un termino valido')