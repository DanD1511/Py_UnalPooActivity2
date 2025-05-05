from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    BIODIESEL = "Biodiésel"
    GAS_NATURAL = "Gas Natural"

class TipoAutomovil(Enum):
    CIUDAD = "Carro de ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Color(Enum):
    BLANCO = "Blanco"
    NEGRO = "Negro"
    ROJO = "Rojo"
    NARANJA = "Naranja"
    AMARILLO = "Amarillo"
    VERDE = "Verde"
    AZUL = "Azul"
    VIOLETA = "Violeta"

class Automovil:
    MULTA_POR_EXCESO = 150_000  # Valor de la multa por exceso de velocidad

    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil,
                 numero_puertas, cantidad_asientos, velocidad_maxima, color, automatico=False):
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._tipo_combustible = tipo_combustible
        self._tipo_automovil = tipo_automovil
        self._numero_puertas = numero_puertas
        self._cantidad_asientos = cantidad_asientos
        self._velocidad_maxima = velocidad_maxima
        self._color = color
        self._velocidad_actual = 0
        self._automatico = automatico
        self._multas = 0  # Contador de multas

    # Métodos get y set
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_motor(self):
        return self._motor

    def set_motor(self, motor):
        self._motor = motor

    def get_tipo_combustible(self):
        return self._tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self._tipo_combustible = tipo_combustible

    def get_tipo_automovil(self):
        return self._tipo_automovil

    def set_tipo_automovil(self, tipo_automovil):
        self._tipo_automovil = tipo_automovil

    def get_numero_puertas(self):
        return self._numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self._numero_puertas = numero_puertas

    def get_cantidad_asientos(self):
        return self._cantidad_asientos

    def set_cantidad_asientos(self, cantidad_asientos):
        self._cantidad_asientos = cantidad_asientos

    def get_velocidad_maxima(self):
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self._velocidad_maxima = velocidad_maxima

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_velocidad_actual(self):
        return self._velocidad_actual

    def set_velocidad_actual(self, velocidad):
        self._velocidad_actual = velocidad

    def get_automatico(self):
        return self._automatico

    def set_automatico(self, automatico):
        self._automatico = automatico

    def get_multas(self):
        return self._multas

    # Método acelerar con control de multas
    def acelerar(self, incremento):
        nueva_velocidad = self._velocidad_actual + incremento
        if nueva_velocidad <= self._velocidad_maxima:
            self._velocidad_actual = nueva_velocidad
            print(f"Velocidad actual: {self._velocidad_actual} km/h")
        else:
            self._multas += 1
            self._velocidad_actual = self._velocidad_maxima  # ajustamos al máximo permitido
            print("Exceso de velocidad. Se ha generado una multa.")
            print(f"Multas acumuladas: {self._multas}")
            print(f"Velocidad actual: {self._velocidad_actual} km/h")

    def desacelerar(self, decremento):
        nueva_velocidad = self._velocidad_actual - decremento
        if nueva_velocidad >= 0:
            self._velocidad_actual = nueva_velocidad
        else:
            self._velocidad_actual = 0
        print(f"Velocidad actual: {self._velocidad_actual} km/h")

    def frenar(self):
        self._velocidad_actual = 0
        print("El automóvil ha frenado. Velocidad actual: 0 km/h")

    def tiene_multas(self):
        return self._multas > 0

    def valor_total_multas(self):
        return self._multas * self.MULTA_POR_EXCESO

    def calcular_tiempo_llegada(self, distancia):
        if self._velocidad_actual > 0:
            tiempo = distancia / self._velocidad_actual
            print(f"Tiempo estimado de llegada: {tiempo:.2f} horas")
            return tiempo
        else:
            print("No se puede calcular el tiempo de llegada porque el vehículo está detenido.")
            return None

    def imprimir(self):
        print("Datos del automóvil:")
        print(f"Marca: {self._marca}")
        print(f"Modelo: {self._modelo}")
        print(f"Motor: {self._motor} L")
        print(f"Tipo de combustible: {self._tipo_combustible.value}")
        print(f"Tipo de automóvil: {self._tipo_automovil.value}")
        print(f"Número de puertas: {self._numero_puertas}")
        print(f"Cantidad de asientos: {self._cantidad_asientos}")
        print(f"Velocidad máxima: {self._velocidad_maxima} km/h")
        print(f"Color: {self._color.value}")
        print(f"Automático: {'Sí' if self._automatico else 'No'}")
        print(f"Velocidad actual: {self._velocidad_actual} km/h")
        print(f"Tiene multas: {'Sí' if self.tiene_multas() else 'No'}")
        print(f"Valor total multas: ${self.valor_total_multas():,.0f} COP")

# Ejemplo de uso
if __name__ == "__main__":
    auto = Automovil(
        marca="Mazda",
        modelo=2023,
        motor=2.0,
        tipo_combustible=TipoCombustible.GASOLINA,
        tipo_automovil=TipoAutomovil.EJECUTIVO,
        numero_puertas=4,
        cantidad_asientos=5,
        velocidad_maxima=180,
        color=Color.ROJO,
        automatico=True
    )

    auto.set_velocidad_actual(100)  #  esto hace que empiece en 100 km/h

    auto.imprimir()
    auto.acelerar(90)  # Excede velocidad máxima, genera multa y ajusta a máximo
    auto.acelerar(5)   # Nueva multa
    auto.desacelerar(50)
    auto.frenar()
    print("-----------------------------------------") #separar para verrificar que luego muestre que si tiene multas 
    auto.imprimir()
    auto.calcular_tiempo_llegada(200)
