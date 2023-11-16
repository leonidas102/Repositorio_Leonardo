class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disp = 0

    def info(self):
        return f"Nombre: {self.nombre}, Precio: ${self.precio}, Cantidad disponible: {self.cantidad_disp}"

    def restar_cantidad(self):
        if self.cantidad_disp > 0:
            self.cantidad_disp -= 1
            return True
        else:
            return False

    def verificar_disponibilidad(self):
        return self.cantidad_disp > 0

    # Getters y setters
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def get_precio(self):
        return self.precio

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def get_cantidad_disp(self):
        return self.cantidad_disp

    def set_cantidad_disp(self, nueva_cantidad):
        self.cantidad_disp = nueva_cantidad


class Snack(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def info(self):
        return super().info() + f", Tipo de snack: {self.tipo}"


class Bebida(Producto):
    def __init__(self, nombre, precio, temperatura):
        super().__init__(nombre, precio)
        self.temperatura = temperatura

    def info(self):
        return super().info() + f", Temperatura de la bebida: {self.temperatura}"


class MaquinaDispensadora:
    def __init__(self):
        self.products = []
        self.totalV = 0.0

    def agregar_producto(self, producto):
        self.products.append(producto)

    def realizar_venta(self, producto, cantidad):
        for prod in self.products:
            if prod.get_nombre() == producto.get_nombre() and prod.verificar_disponibilidad():
                if prod.get_cantidad_disp() >= cantidad:
                    prod.set_cantidad_disp(prod.get_cantidad_disp() - cantidad)
                    self.totalV += prod.get_precio() * cantidad
                    return f"Venta realizada. Total a pagar: ${prod.get_precio() * cantidad}"
                else:
                    return "No hay suficiente cantidad disponible."
        return "Producto no encontrado o agotado."

    def total_ventas(self):
        return f"Total de ventas: ${self.totalV}"


# Ejemplo de uso:
snack1 = Snack("Papas", 1.5, "Saladas")
bebida1 = Bebida("Refresco", 2.0, "Fría")

maquina = MaquinaDispensadora()
maquina.agregar_producto(snack1)
maquina.agregar_producto(bebida1)

print(snack1.info())  # Mostrar información del snack
print(bebida1.info())  # Mostrar información de la bebida

print(maquina.realizar_venta(snack1, 2))  # Realizar venta de 2 snacks
print(maquina.total_ventas())