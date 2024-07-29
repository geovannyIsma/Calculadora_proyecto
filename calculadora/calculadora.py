from calculadora.factory import FabricaDeOperaciones

"""
Patron de diseño Singleton
--------------------------
En que consiste?
El patrón de diseño Singleton consiste en garantizar que una clase tenga una única instancia 
y proporcionar un punto de acceso global a ella. Esto es útil cuando se necesita una única 
instancia de una clase para coordinar acciones en todo el sistema.

En este caso, se implementa el patrón Singleton para la calculadora. La clase Calculadora
tiene un atributo de clase _instancia que guarda la única instancia de la clase. El método
__new__ se encarga de crear la instancia si no existe y devolverla en caso contrario. De esta
forma, se garantiza que solo exista una instancia de la clase Calculadora en todo el sistema.

Además, la clase Calculadora tiene un método ejecutar que recibe una operación y una serie de
argumentos y delega la ejecución de la operación a la estrategia correspondiente. La clase
FabricaDeOperaciones se encarga de obtener la estrategia adecuada para la operación solicitada.

"""
class Calculadora:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Calculadora, cls).__new__(cls)
        return cls._instancia

    def ejecutar(self, operacion, *args):
        estrategia = FabricaDeOperaciones.obtener_estrategia(operacion)
        return estrategia.ejecutar(*args)