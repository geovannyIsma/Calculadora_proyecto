from calculadora.strategies import *


class FabricaDeOperaciones:
    @staticmethod
    def obtener_estrategia(operacion):
        estrategias = {
            'suma': EstrategiaSuma,
            'resta': EstrategiaResta,
            'multiplicacion': EstrategiaMultiplicacion,
            'division': EstrategiaDivision,
            'potencia': EstrategiaPotencia,
            'raiz_cuadrada': EstrategiaRaizCuadrada,
            'logaritmo': EstrategiaLogaritmo,
            'logaritmo_natural': EstrategiaLogaritmoNatural,
            'exponencial': EstrategiaExponencial,
            'seno': EstrategiaSeno,
            'coseno': EstrategiaCoseno,
            'tangente': EstrategiaTangente,
            'arcoseno': EstrategiaArcoseno,
            'arcocoseno': EstrategiaArcocoseno,
            'arcotangente': EstrategiaArcotangente,
            'sinh': EstrategiaSinh,
            'cosh': EstrategiaCosh,
            'tanh': EstrategiaTanh,
            'factorial': EstrategiaFactorial,
            'modulo': EstrategiaModulo,
            'potencia_de_diez': EstrategiaPotenciaDeDiez,
            'inversa': EstrategiaInversa,
        }
        if operacion in estrategias:
            return estrategias[operacion]()
        else:
            raise ValueError("Operación desconocida")