class CuentaBancaria:
    def __init__(self, nombre, apellido, numero_cuenta, tipo_cuenta, saldo=0.0):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta  # "ahorros" o "corriente"
        self.saldo = saldo

    def imprimir_datos(self):
        print(f"Titular: {self.nombre} {self.apellido}")
        print(f"Numero de cuenta: {self.numero_cuenta}")
        print(f"Tipo de cuenta: {self.tipo_cuenta}")
        print(f"Saldo actual: {self.saldo:.2f}")

    def consultar_saldo(self):
        return self.saldo

    def consignar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Consignacion exitosa. Nuevo saldo: {self.saldo:.2f}")
        else:
            print("La cantidad debe ser mayor a cero.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
        elif cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.saldo:.2f}")


cuenta1 = CuentaBancaria("Pedro", "Perez", "123456789", "ahorros")
cuenta1.imprimir_datos()
cuenta1.consignar(500)
cuenta1.retirar(200)
cuenta1.imprimir_datos()
