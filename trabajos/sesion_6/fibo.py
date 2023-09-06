
n = int(input("Ingrese la cantidad de dígitos de la serie de Fibonacci que desea ver: "))

a, b = 0, 1

digitos = 0

if n <= 0:
    print("Por favor, ingrese un número válido mayor que cero.")
else:
    print("Serie de Fibonacci con", n, "dígitos:")
    while digitos < n:

        print(a, end=' ')
        digitos+= len(str(a))

        a, b = b, a + b

print()
