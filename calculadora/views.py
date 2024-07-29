from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calculadora.calculadora import Calculadora


@csrf_exempt
def calcular(request):
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
