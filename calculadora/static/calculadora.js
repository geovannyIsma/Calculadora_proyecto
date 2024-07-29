let expresionActual = '';
let valorActual = '0';
let resultadoCalculado = false;

function actualizarPantalla() {
    document.getElementById('expresion-completa').textContent = expresionActual;
    document.getElementById('valor-actual').textContent = formatarNumero(valorActual);
}

function formatarNumero(num) {
    return new Intl.NumberFormat().format(num);
}

function manejarNumero(numero) {
    if (resultadoCalculado) {
        expresionActual = '';
        valorActual = numero;
        resultadoCalculado = false;
    } else {
        if (valorActual === '0') {
            valorActual = numero;
        } else {
            valorActual += numero;
        }
    }
    actualizarPantalla();
}

function manejarOperacion(operacion) {
    if (resultadoCalculado) {
        expresionActual = valorActual;
        resultadoCalculado = false;
    } else {
        expresionActual += valorActual;
    }

    switch (operacion) {
        case 'suma':
            expresionActual += ' + ';
            break;
        case 'resta':
            expresionActual += ' - ';
            break;
        case 'multiplicacion':
            expresionActual += ' * ';
            break;
        case 'division':
            expresionActual += ' / ';
            break;
        case 'potencia':
            expresionActual += ' ^ ';
            break;
        case 'modulo':
            expresionActual += ' % ';
            break;
        default:
            return;
    }

    valorActual = '0';
    actualizarPantalla();
}

function manejarOperacionUnaria(operacion) {
    let valor = parseFloat(valorActual);
    let pantallaExpresion = '';

    switch (operacion) {
        case 'raiz_cuadrada':
            pantallaExpresion = `√(${valorActual})`;
            break;
        case 'logaritmo':
            pantallaExpresion = `log(${valorActual})`;
            break;
        case 'logaritmo_natural':
            pantallaExpresion = `ln(${valorActual})`;
            break;
        case 'exponencial':
            pantallaExpresion = `exp(${valorActual})`;
            break;
        case 'seno':
            pantallaExpresion = `sin(${valorActual})`;
            break;
        case 'coseno':
            pantallaExpresion = `cos(${valorActual})`;
            break;
        case 'tangente':
            pantallaExpresion = `tan(${valorActual})`;
            break;
        case 'arcoseno':
            pantallaExpresion = `asin(${valorActual})`;
            break;
        case 'arcocoseno':
            pantallaExpresion = `acos(${valorActual})`;
            break;
        case 'arcotangente':
            pantallaExpresion = `atan(${valorActual})`;
            break;
        case 'sinh':
            pantallaExpresion = `sinh(${valorActual})`;
            break;
        case 'cosh':
            pantallaExpresion = `cosh(${valorActual})`;
            break;
        case 'tanh':
            pantallaExpresion = `tanh(${valorActual})`;
            break;
        case 'factorial':
            pantallaExpresion = `${valorActual}!`;
            break;
        case 'modulo':
            pantallaExpresion = `(${valorActual}) %`;
            break;
        case 'potencia_de_diez':
            pantallaExpresion = `10^(${valorActual})`;
            break;
        case 'inversa':
            pantallaExpresion = `1/(${valorActual})`;
            break;
        default:
            return;
    }

    expresionActual = pantallaExpresion;
    actualizarPantalla();
    ejecutarOperacion(operacion, valor);
}

function ejecutarOperacion(operacion, a, b = null) {
    const formData = new FormData();
    formData.append('operation', operacion);
    formData.append('a', a);
    if (b !== null) {
        formData.append('b', b);
    }

    fetch('/calculate/', {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                throw new Error(data.error);
            }
            valorActual = redondearNumero(data.result);
            resultadoCalculado = true;
            actualizarPantalla();
        })
        .catch(error => {
            valorActual = 'Error';
            console.error('Error:', error);
            actualizarPantalla();
        });
}

function redondearNumero(num, decimales = 10) {
    return Number(num.toFixed(decimales));
}

function manejarIgual() {
    if (resultadoCalculado) {
        expresionActual = valorActual;
    } else {
        expresionActual += valorActual;
    }

    try {
        const resultado = eval(expresionActual.replace('^', '**'));
        valorActual = resultado.toString();
        expresionActual = '';
        resultadoCalculado = true;
        actualizarPantalla();
    } catch (error) {
        valorActual = 'Error';
        actualizarPantalla();
    }
}

function manejarLimpiar() {
    expresionActual = '';
    valorActual = '0';
    resultadoCalculado = false;
    actualizarPantalla();
}

function manejarBorrar() {
    if (resultadoCalculado) {
        expresionActual = '';
        valorActual = '0';
        resultadoCalculado = false;
    } else {
        if (valorActual.length > 1) {
            valorActual = valorActual.slice(0, -1);
        } else {
            valorActual = '0';
        }
    }
    actualizarPantalla();
}

document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', () => {
        const valor = button.getAttribute('data-value');

        if (!isNaN(valor)) {
            manejarNumero(valor);
        } else if (valor === 'igual') {
            manejarIgual();
        } else if (valor === 'limpiar') {
            manejarLimpiar();
        } else if (valor === 'borrar') {
            manejarBorrar();
        } else if (['suma', 'resta', 'multiplicacion', 'division', 'potencia', 'modulo'].includes(valor)) {
            manejarOperacion(valor);
        } else {
            manejarOperacionUnaria(valor);
        }
    });
});

actualizarPantalla();