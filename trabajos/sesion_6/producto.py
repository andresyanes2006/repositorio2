numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

resultado = 0

if numero1 == 0 or numero2 == 0:
    resultado = 0
else:
    for i in range(abs(numero2)):
        resultado += abs(numero1)

if (numero1 < 0 and numero2 > 0) or (numero1 > 0 and numero2 < 0):
    resultado = -resultado
print(f"El producto de {numero1} y {numero2} es: {resultado}")