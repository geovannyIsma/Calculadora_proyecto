import math

"""
Patron de diseño Strategy
--------------------------
En que consiste?
El patrón de diseño Strategy consiste en definir una familia de algoritmos,
encapsular cada uno de ellos y hacerlos intercambiables. De esta forma, el
algoritmo puede variar independientemente de los clientes que lo utilizan.

En este caso, se implementa el patrón Strategy para la calculadora. Se definen
diferentes estrategias que representan las operaciones que se pueden realizar
con la calculadora, como suma, resta, multiplicación, división, etc. Cada una
de estas estrategias implementa un método ejecutar que realiza la operación
correspondiente. De esta forma, se puede cambiar la estrategia de la calculadora en tiempo de
ejecución, permitiendo que el usuario seleccione la operación que desea realizar.

En este caso, se implementan las siguientes estrategias:
- Suma
- Resta
- Multiplicación
- División
- Potencia
- Raíz cuadrada
- Logaritmo
- Logaritmo natural
- Exponencial
- Seno
- Coseno
- Tangente
- Arcoseno
- Arcocoseno
- Arcotangente
- Seno hiperbólico
- Coseno hiperbólico
- Tangente hiperbólica
- Factorial
- Módulo
- Potencia de diez
- Inversa
"""


class EstrategiaSuma:
    def ejecutar(self, a, b):
        return a + b


class EstrategiaResta:
    def ejecutar(self, a, b):
        return a - b


class EstrategiaMultiplicacion:
    def ejecutar(self, a, b):
        return a * b


class EstrategiaDivision:
    def ejecutar(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b


class EstrategiaPotencia:
    def ejecutar(self, a, b):
        return math.pow(a, b)


class EstrategiaRaizCuadrada:
    def ejecutar(self, a):
        if a < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        return math.sqrt(a)


class EstrategiaLogaritmo:
    def ejecutar(self, a, base=10):
        if a <= 0:
            raise ValueError("El logaritmo solo está definido para números positivos")
        return math.log(a, base)


class EstrategiaLogaritmoNatural:
    def ejecutar(self, a):
        if a <= 0:
            raise ValueError("El logaritmo natural solo está definido para números positivos")
        return math.log(a)


class EstrategiaExponencial:
    def ejecutar(self, a):
        return math.exp(a)


class EstrategiaSeno:
    def ejecutar(self, a):
        return math.sin(math.radians(a))


class EstrategiaCoseno:
    def ejecutar(self, a):
        return math.cos(math.radians(a))


class EstrategiaTangente:
    def ejecutar(self, a):
        return math.tan(math.radians(a))


class EstrategiaArcoseno:
    def ejecutar(self, a):
        if a < -1 or a > 1:
            raise ValueError("El arcoseno solo está definido para valores en el rango [-1, 1]")
        return math.degrees(math.asin(a))


class EstrategiaArcocoseno:
    def ejecutar(self, a):
        if a < -1 or a > 1:
            raise ValueError("El arcocoseno solo está definido para valores en el rango [-1, 1]")
        return math.degrees(math.acos(a))


class EstrategiaArcotangente:
    def ejecutar(self, a):
        return math.degrees(math.atan(a))


class EstrategiaSinh:
    def ejecutar(self, a):
        return math.sinh(a)


class EstrategiaCosh:
    def ejecutar(self, a):
        return math.cosh(a)


class EstrategiaTanh:
    def ejecutar(self, a):
        return math.tanh(a)


class EstrategiaFactorial:
    def ejecutar(self, a):
        if not a.is_integer() or a < 0:
            raise ValueError("El factorial solo está definido para enteros no negativos")
        return math.factorial(int(a))


class EstrategiaModulo:
    def ejecutar(self, a, b):
        return a % b


class EstrategiaPotenciaDeDiez:
    def ejecutar(self, a):
        return 10 ** a


class EstrategiaInversa:
    def ejecutar(self, a):
        if a == 0:
            raise ValueError("No se puede dividir por cero")
        return 1 / a
