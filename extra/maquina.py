class Producto:
    def __init__(self, nombre, precio, cantidad_disponible=0):
        self._nombre = nombre
        self._precio = precio
        self._cantidad_disponible = cantidad_disponible

    # Getters y setters para los atributos de la clase Producto
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def get_cantidad_disponible(self):
        return self._cantidad_disponible

    def set_cantidad_disponible(self, nueva_cantidad):
        self._cantidad_disponible = nueva_cantidad

    def obtener_info(self):
        return f"Nombre: {self._nombre}, Precio: {self._precio}, Cantidad disponible: {self._cantidad_disponible}"

    def restar_cantidad(self):
        if self._cantidad_disponible > 0:
            self._cantidad_disponible -= 1
        else:
            print("Producto agotado")

    def verificar_disponibilidad(self):
        return self._cantidad_disponible > 0


class Snack(Producto):
    def __init__(self, nombre, precio, tipo, cantidad_disponible=0):
        super().__init__(nombre, precio, cantidad_disponible)
        self._tipo = tipo

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre}, Tipo: {self._tipo}"


class Bebida(Producto):
    def __init__(self, nombre, precio, tamaño, cantidad_disponible=0):
        super().__init__(nombre, precio, cantidad_disponible)
        self._tamaño = tamaño

    def get_tamaño(self):
        return self._tamaño

    def set_tamaño(self, nuevo_tamaño):
        self._tamaño = nuevo_tamaño

    def obtener_info(self):
        info_padre = super().obtener_info()
        return f"{info_padre}, Tamaño: {self._tamaño}"


class MaquinaDispensadora:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, nombre_producto):
        for producto in self.productos:
            if producto.get_nombre() == nombre_producto:
                if producto.verificar_disponibilidad():
                    producto.restar_cantidad()
                    print(f"Venta realizada: {producto.get_nombre()} - Precio: {producto.get_precio()}")
                else:
                    print(f"{producto.get_nombre()} agotado")
                return
        print("Producto no encontrado")

    def total_ventas(self):
        total = 0
        for producto in self.productos:
            total += producto.get_precio() * (producto.get_cantidad_disponible() < 0)
        return total


# Ejemplo de uso:
snack_1 = Snack("Galletas", 15, "Dulce", 10)
bebida_1 = Bebida("Refresco", 20, "Grande", 5)

maquina = MaquinaDispensadora()
maquina.agregar_producto(snack_1)
maquina.agregar_producto(bebida_1)

maquina.realizar_venta("Galletas")
maquina.realizar_venta("Galletas")
maquina.realizar_venta("Refresco")

print(f"Total ventas: {maquina.total_ventas()}")