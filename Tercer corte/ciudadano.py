class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_cedula(self, cedula):
        if 8 <= len(cedula) <= 10:
            self.__cedula = cedula
        else:
            print("La cédula debe tener entre 8 y 10 dígitos.")

    def get_cedula(self):
        return self.__cedula

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo mayor que cero.")

    def get_edad(self):
        return self.__edad

    def mostrar(self):
        print(f"Nombre: {self.__nombre} - Edad: {self.__edad} - CC: {self.__cedula}")

    def esMayorDeEdad(self):
        return self.__edad >= 18


class Cocinero(Ciudadano):
    def __init__(self, nombre, cedula, edad, especialidad, experiencia):
        super().__init__(nombre, cedula, edad)
        self.__especialidad = especialidad
        self.__experiencia = experiencia

    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    def get_especialidad(self):
        return self.__especialidad

    def set_experiencia(self, experiencia):
        self.__experiencia = experiencia

    def get_experiencia(self):
        return self.__experiencia

    def preparar_plato(self):
        return f"Preparando plato de la especialidad {self.__especialidad}"


class Medico(Ciudadano):
    def __init__(self, nombre, cedula, edad, especializacion, consultorio):
        super().__init__(nombre, cedula, edad)
        self.__especializacion = especializacion
        self.__consultorio = consultorio

    def set_especializacion(self, especializacion):
        self.__especializacion = especializacion

    def get_especializacion(self):
        return self.__especializacion

    def set_consultorio(self, consultorio):
        self.__consultorio = consultorio

    def get_consultorio(self):
        return self.__consultorio

    def realizar_diagnostico(self):
        return f"Realizando diagnóstico de {self.__especializacion}"


class Ingeniero(Ciudadano):
    def __init__(self, nombre, cedula, edad, Calcular, construir):
        super().__init__(nombre, cedula, edad)
        self.__Calcular = Calcular
        self.__construir = construir

    def set_Calcular(self, Calcular):
        self.__Calcular = Calcular

    def get_especialidad(self):
        return self.__Calcular

    def set_proyecto_actual(self, construir):
        self.__construir = construir

    def get_proyecto_actual(self):
        return self.__construir

    def resolver_problema(self):
        return f"Resolviendo problema en el proyecto {self.__construir}"