
class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "blanco" or color == "negro":
            self.color = color


class Auto:
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro, cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos[0]
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados


    def verificarIntegridad(self, registro):
        if Asiento.asiento[0] == registro and Motor.registro:
            return "Auto original"
        else:
            return "Las piezas no son originales"

    def cantidadAsientos():
        numeroAsientos = 0
        if Asiento.asientos != []:
            for asiento in Asiento.asientos:
                if asiento != []:
                    numeroAsientos += 1
        return numeroAsientos

class Motor:
    
    def __init__(self, tipo, numeroCilindros, registro):
        self.tipo = tipo
        self.numeroCilindros = numeroCilindros
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "gasolina":
            self.tipo = tipo
        if tipo == "electrico":
            self.tipo = tipo