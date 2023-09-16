def calcular_cuadrado():
    num = int(input("Ingrese un número entero: "))
    cuadrado = num ** 2
    print("El cuadrado de", num, "es:", cuadrado)

def calcular_producto():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    producto = num1 * num2
    print("El producto de", num1, "y", num2, "es:", producto)

# Llamada a la primera función
calcular_cuadrado()

# Llamada a la segunda función
calcular_producto()
