# Calculadora modular en Python

def presentacion():
    print("====================================")
    print("  CALCULADORA MODULAR EN PYTHON     ")
    print("====================================")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# Función para multiplicar
def multiplicar(a, b):
    return a * b

# Función para dividir
def dividir(a, b):
    if b == 0:
        return "Error: no es posible dividir entre cero"
    return a / b


if __name__ == "__main__":
    presentacion()
    print("Suma:", sumar(10, 5))
    print("Resta:", restar(10, 5))
    print("Multiplicación:", multiplicar(10, 5))
    print("División:", dividir(10, 5))
    print("División entre cero:", dividir(10, 0))