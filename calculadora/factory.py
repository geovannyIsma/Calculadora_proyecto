from calculadora.strategies import *

"""
Patron de diseño Factory
------------------------
En que consiste?
El patrón de diseño Factory consiste en definir una interfaz para crear objetos, pero
dejar que las subclases decidan qué clase instanciar. De esta forma, se delega la creación
de objetos a las subclases, permitiendo que el código cliente trabaje con la interfaz
común sin necesidad de conocer la implementación concreta.

por que se usa?
En este caso, se implementa el patrón Factory para la calculadora. La clase FabricaDeOperaciones
tiene un método estático obtener_estrategia que recibe el nombre de una operación y devuelve la
estrategia correspondiente. De esta forma, se puede obtener la estrategia adecuada para una
operación sin necesidad de conocer la implementación concreta de cada estrategia.
"""


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
