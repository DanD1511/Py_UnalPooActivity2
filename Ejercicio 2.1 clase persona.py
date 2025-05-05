from datetime import datetime

class Persona:
    """
    Clase Persona que almacena datos personales básicos.
    """

    def __init__(self, nombre, apellidos, numero_documento, ano_nacimiento, pais_nacimiento, genero):
        """
        Constructor de la clase Persona.
        :param nombre: Nombres de la persona.
        :param apellidos: Apellidos de la persona.
        :param numero_documento: Número de documento de identidad.
        :param ano_nacimiento: Año de nacimiento.
        :param pais_nacimiento: País de nacimiento.
        :param genero: Género de la persona ('H' o 'M').
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.ano_nacimiento = ano_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero

    def calcular_edad(self):
        """
        Calcula la edad actual de la persona a partir del año de nacimiento.
        :return: Edad actual.
        """
        ano_actual = datetime.now().year
        return ano_actual - self.ano_nacimiento

    def mostrar_informacion(self):
        """
        Muestra toda la información de la persona.
        """
        print(f"Nombre : {self.nombre}")
        print(f"Apellidos:{self.apellidos}")
        print(f"Número de documento : {self.numero_documento}")
        print(f"Año de nacimiento   : {self.ano_nacimiento}")
        print(f"Edad                : {self.calcular_edad()} años")
        print(f"País de nacimiento  : {self.pais_nacimiento}")
        print(f"Género              : {'Hombre' if self.genero == 'H' else 'Mujer'}")


# probando que si de
persona1 = Persona("Laura", "Gómez Ramírez", "123456789", 1995, "Colombia", 'M')
persona2 = Persona("Carlos", "Pérez Martínez", "987654321", 1980, "México", 'H')

persona1.mostrar_informacion()
print("-----------------------------")
persona2.mostrar_informacion()
