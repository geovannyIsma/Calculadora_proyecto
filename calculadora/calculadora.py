from calculadora.factory import FabricaDeOperaciones


# patrón singleton
class Calculadora:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Calculadora, cls).__new__(cls)
        return cls._instancia

    def ejecutar(self, operacion, *args):
        estrategia = FabricaDeOperaciones.obtener_estrategia(operacion)
        return estrategia.ejecutar(*args)