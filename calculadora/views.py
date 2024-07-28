from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from calculadora.calculadora import Calculadora


@csrf_exempt
def calculate(request):
    if request.method == 'POST':
        operation = request.POST.get('operation')
        a = request.POST.get('a')
        b = request.POST.get('b', None)

        try:
            a = float(a)
            if b is not None:
                b = float(b)
        except ValueError:
            return JsonResponse({'error': 'Invalid input'}, status=400)

        calculator = Calculadora()
        try:
            if b is not None:
                result = calculator.ejecutar(operation, a, b)
            else:
                result = calculator.ejecutar(operation, a)
            return JsonResponse({'result': result})
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'calculate.html')
