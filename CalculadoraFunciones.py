calcular=["sumar:" , "restar:", "dividir:" , "multiplicar:", "elevado: "] 
def menu():
    for i in range (len(calcular)):
        print(f"{i+1} {calcular[i]}")

def resta(a,b):
    print(a-b)

def suma(a,b):
    print(a+b)

def multiplicacion(a,b):
    print(a*b)
    
def division(a,b):
    try:
        print(a/b)
    except Exception:
        print("no se puede dividir por cero")

def elevado(a,b):
    print(a**b)

def mein():
    try:
        menu()
        opcion=int(input("ingrese una opcion"))
        while opcion >= 1 and opcion <= 5:
            a = int(input("deme un numero :"))
            b = int(input("deme un numero :"))
            if opcion == 1:
                suma(a,b)
                mein()
            elif opcion==2:
                resta(a,b)
                mein()
            elif opcion==3:
                division(a,b)
                mein()
            elif opcion==4:
                multiplicacion(a,b)
                mein()
            elif opcion == 5 :
                elevado(a,b)
                mein()
            else:
                print("salir enter :D")
    except Exception:
        print("porfavor coloque un digito no una letra o simbolo")

mein()  
