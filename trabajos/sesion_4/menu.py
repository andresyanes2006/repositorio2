while True:
    menu=int(input('''
    Seleciona el numero del programas que quieres correr 
                   
    1. Verficacr si letra es vocal o consonante
    2. Tiempo de parqueo
    3. Tipo de triangulo
    0. salir
    '''))
    if menu==1:
        letra=str(input('Ingrese una letra del abecedario: '))
        if (letra.lower()=='a') or (letra.lower()=='e') or (letra.lower()=='i') or (letra.lower()=='o') or (letra.lower()=='u'):
            print('Es una vocal')
        else:
            print('Es una consonante')

    elif menu==2:
        cobro=139
        t=int(input('¿Cuantos minutos tardo?'))
        subtotal=(cobro*t)
        iva=subtotal*(19/100)
        total=subtotal+iva
        resultado = round(total / 50) * 50 
        print('El total a pagar es:',resultado)

    elif menu==3:
        a=int(input('Ingrese medida uno: '))
        b=int(input('Ingrese medida dos: '))
        c=int(input('Ingrese medida tres: '))
        if (a+b>c)and(a+c>b)and(b+c>a):
            if (a==b)and(b==c)and(c==a):
                 print('el triangulo es equilatero')
            elif (a==b!=c)or(a==c!=b)or(b==c!=a):
                print('el triangulo es isoseles')
            elif (a!=b)and(b!=c)and(c!=a):
                 print('el triangulo es escaleno')
        else:
            print('no se puede hacer un triangulo con esas medidas')
    else:
        break

 
