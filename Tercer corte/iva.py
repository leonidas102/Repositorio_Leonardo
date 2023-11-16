class Articulo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_bruto(self):
        return self.precio

class ArticuloExento(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

class ArticuloIVA5(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def calcular_precio_bruto(self):
        return self.precio * 1.05

class ArticuloIVA19(Articulo):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)

    def calcular_precio_bruto(self):
        return self.precio * 1.19

# Función para calcular el precio bruto y el valor del IVA de una lista de artículos
def calcular_precio_iva(articulos):
    total_precio_bruto = 0
    total_valor_iva = 0

    for articulo in articulos:
        precio_bruto = articulo.calcular_precio_bruto()
        total_precio_bruto += precio_bruto

        if isinstance(articulo, ArticuloExento):
            valor_iva = 0
        elif isinstance(articulo, ArticuloIVA5):
            valor_iva = precio_bruto * 0.05
        elif isinstance(articulo, ArticuloIVA19):
            valor_iva = precio_bruto * 0.19

        total_valor_iva += valor_iva

    return total_precio_bruto, total_valor_iva