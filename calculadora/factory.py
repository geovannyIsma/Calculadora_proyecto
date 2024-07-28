from calculadora.strategies.strategies import *


class FabricaDeOperaciones:
    @staticmethod
    def obtener_estrategia(operacion):
        estrategias = {
            'add': EstrategiaSuma,
            'subtract': EstrategiaResta,
            'multiply': EstrategiaMultiplicacion,
            'divide': EstrategiaDivision,
            'power': EstrategiaPotencia,
            'sqrt': EstrategiaRaizCuadrada,
            'log': EstrategiaLogaritmo,
            'ln': EstrategiaLogaritmoNatural,
            'exp': EstrategiaExponencial,
            'sin': EstrategiaSeno,
            'cos': EstrategiaCoseno,
            'tan': EstrategiaTangente,
            'asin': EstrategiaArcoseno,
            'acos': EstrategiaArcocoseno,
            'atan': EstrategiaArcotangente,
            'sinh': EstrategiaSinh,
            'cosh': EstrategiaCosh,
            'tanh': EstrategiaTanh,
            'factorial': EstrategiaFactorial,
            'mod': EstrategiaModulo,
            'power_of_ten': EstrategiaPotenciaDeDiez,
            'inverse': EstrategiaInversa,
        }
        if operacion in estrategias:
            return estrategias[operacion]()
        else:
            raise ValueError("Operación desconocida")