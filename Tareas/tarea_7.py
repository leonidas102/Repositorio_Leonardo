import math
print('Seleccione el codigo a ejecutar: \n\
 1.vectores \n 2.N perfectos')
r=input('Ingrese alguna de las opciones anteriores: ')

if (r=="1") or (r.lower()=="vectores" ):
    def coordenadas():
      x1=float(input("Ingresa la coordenada x del punto de origen: "))
      y1=float(input("Ingresa la coordenada y del punto de origen: "))
      x2=float(input("Ingresa la coordenada x del punto final: "))
      y2=float(input("Ingresa la coordenada y del punto final: "))
      return x1, y1, x2, y2

    def calcular_modulo(x1, y1, x2, y2):
      modulo=math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
      return modulo

    def calcular_componentes_rectangulares(x1, y1, x2, y2):
      x=x2-x1
      y=y2-y1
      return x, y

    def main():
      print("Calculadora de módulo y componentes rectangulares de un vector")
      x1,y1,x2,y2=coordenadas()
    
      modulo=calcular_modulo(x1, y1, x2, y2)
      x, y=calcular_componentes_rectangulares(x1, y1, x2, y2)
    
      print(f"El módulo del vector es: {round(modulo,2)}")
      print(f"Las componentes rectangulares del vector son:")
      print(f"Componente en x: {x}")
      print(f"Componente en y: {y}")

if (r=="2") or (r.lower()=="n perfectos" ):
   def calcular_divisores(numero):
    divisores=[]
    for i in range(1,numero):
        if numero%i==0:
            divisores.append(i)
    return divisores

def es_numero_perfecto(numero):
    suma_divisores=sum(calcular_divisores(numero))
    return suma_divisores==numero

def imprimir_numeros_perfectos(cantidad):
    numeros_perfectos=[]
    numero=1
    while len(numeros_perfectos)<cantidad:
        if es_numero_perfecto(numero):
            numeros_perfectos.append(numero)
        numero+=1

    print(f"Los {cantidad} primeros números perfectos son:")
    for numero in numeros_perfectos:
        print(numero)
        
cantidad=int(input("Ingrese la cantidad de números perfectos a imprimir (máximo 4): "))

if cantidad>4:
    cantidad=4

imprimir_numeros_perfectos(cantidad)



if __name__=="__main__":
    main()