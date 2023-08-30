import fc_externa
import fun3

def main():
    nombre= input('ingrese su nombre: ')
    apellido=input('ingrese su apellido ')
    fc_externa.matrix(nombre, apellido)
    print(f'ejecutado desde  {__name__}')
    print('******')
    a=int(input('ingrese numero '))
    b=int(input('ingrese numero '))
    fun3.suma(a,b)
    print('******')

if __name__=="__main__":
    main()

   
