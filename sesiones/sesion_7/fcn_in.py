import fcn_ext

def main():
    a=int(input('ingrese un numero'))
    b=int(input('ingrese otro numero'))
    r=fcn_ext.suma(a,b)
    print(r)
    print(f'ejecutado desde{__name__}') 

if __name__=="main_":
    main()