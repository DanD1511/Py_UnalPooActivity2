from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    """
    Clase que representa un planeta del sistema solar.
    """

    def __init__(self, nombre=None, cantidad_satelites=0, masa_kg=0.0,
                 volumen_km3=0.0, diametro_km=0, distancia_media_sol=0,
                 tipo_planeta=TipoPlaneta.TERRESTRE, observable=False,
                 periodo_orbital=0.0, periodo_rotacion=0.0):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa_kg = masa_kg
        self.volumen_km3 = volumen_km3
        self.diametro_km = diametro_km
        self.distancia_media_sol = distancia_media_sol
        self.tipo_planeta = tipo_planeta
        self.observable = observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacion = periodo_rotacion

    def mostrar_informacion(self):
        """
        Imprime en pantalla todos los atributos del planeta.
        """
        print(f"Nombre                 : {self.nombre}")
        print(f"Cantidad de satélites : {self.cantidad_satelites}")
        print(f"Masa (kg)             : {self.masa_kg:.2e}")
        print(f"Volumen (km³)         : {self.volumen_km3:.2e}")
        print(f"Diámetro (km)         : {self.diametro_km}")
        print(f"Distancia al sol (millones km): {self.distancia_media_sol}")
        print(f"Tipo de planeta       : {self.tipo_planeta.value}")
        print(f"Visible a simple vista: {'Sí' if self.observable else 'No'}")
        print(f"Densidad (kg/km³)     : {self.calcular_densidad():.2e}")
        print(f"¿Es planeta exterior? : {'Sí' if self.es_planeta_exterior() else 'No'}")
        print(f"Período orbital (años): {self.periodo_orbital}")
        print(f"Período rotación (días): {self.periodo_rotacion}")

    def calcular_densidad(self):
        """
        Calcula y devuelve la densidad del planeta.
        :return: densidad en kg/km³
        """
        if self.volumen_km3 > 0:
            return self.masa_kg / self.volumen_km3
        else:
            return 0.0

    def es_planeta_exterior(self):
        """
        Determina si el planeta es exterior (distancia > cinturon asteroides).
        :return: True si es exterior, False si es interior.
        """
        return self.distancia_media_sol > 149597870 * 3.4


# Ejemplo verificar que de 
planeta1 = Planeta(nombre="Marte",
    cantidad_satelites=2,
    masa_kg=6.417e23,
    volumen_km3=1.6318e11,
    diametro_km=6792,
    distancia_media_sol=228,
    tipo_planeta=TipoPlaneta.TERRESTRE,
    observable=True,
    periodo_orbital=1.88,
    periodo_rotacion=1.03
    )
    

planeta1.mostrar_informacion()
