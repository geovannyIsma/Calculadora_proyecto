from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calculadora.calculadora import Calculadora


@csrf_exempt
def calcular(request):
    """
    Vista para manejar solicitudes POST y realizar cálculos.

    Esta vista recibe una solicitud POST con los parámetros 'operation', 'a' y opcionalmente 'b'.
    Realiza el cálculo utilizando la clase Calculadora y devuelve el resultado en formato JSON.

    Parámetros:
    - request: La solicitud HTTP.

    Retorna:
    - JsonResponse: Un objeto JSON con el resultado del cálculo o un mensaje de error.
    - HttpResponse: Una respuesta HTTP con la plantilla 'calculate.html' para solicitudes GET.

    Manejo de errores:
    - Si los parámetros 'a' o 'b' no son números válidos, devuelve un error JSON con el mensaje 'Entrada no válida'.
    - Si ocurre un error en el cálculo, devuelve un error JSON con el mensaje del error.

    Decoradores:
    - @csrf_exempt: Exime esta vista de la verificación CSRF.
    """
    if request.method == 'POST':
        operacion = request.POST.get('operation')
        a = request.POST.get('a')
        b = request.POST.get('b', None)

        try:
            a = float(a)
            if b is not None:
                b = float(b)
        except ValueError:
            return JsonResponse({'error': 'Entrada no válida'}, status=400)

        calculadora = Calculadora()
        try:
            if b is not None:
                resultado = calculadora.ejecutar(operacion, a, b)
            else:
                resultado = calculadora.ejecutar(operacion, a)
            return JsonResponse({'result': resultado})
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'calculate.html')
