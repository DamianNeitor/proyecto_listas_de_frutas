lista_fruta=["manzana", "platano","uva","mandarina","cacao","carrito de compra"," salir"]
lista_precio_fruta=[1000,2000,5000,7000,10000]
lista_cantidad=[0,0,0,0,0]
lista_pago=["pagar con efectivo","pagar con credito", "pagar con debito"]
carrito = []
def mostrarmenu():
    for i in range (len(lista_fruta)):
        print(f"{i+1} {lista_fruta[i]}")

def comprar():
    while True:
        try:
            global x
            mostrarmenu()
            print("_______________________________________________________________")
            opcion=int(input("escoje una opcion"))
            print("_____________________________________________________________-")
            if opcion >= 1 and opcion <= 7:
                print(f"escojistes la opcion {lista_fruta[opcion-1]}")
                if opcion == 1 :
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar"))
                    print(f"{cantidad_fruta + lista_cantidad[0]}")
                    x=cantidad_fruta * lista_precio_fruta[0]
                    print(x)
                    tipo_de_pago()
                elif opcion == 2:
                    cantidad_fruta= int(input("ingrese la cantidad de fruta que desea llevar"))
                    print(f"{cantidad_fruta + lista_cantidad[1]}")
                    x=cantidad_fruta * lista_precio_fruta[1]
                    print(x)
                    tipo_de_pago()
                elif opcion == 3:
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar"))
                    print({cantidad_fruta + lista_cantidad[2]})
                    x=cantidad_fruta * lista_precio_fruta[2]
                    print(x)
                    tipo_de_pago()
                elif opcion == 4:
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar"))
                    print({cantidad_fruta + lista_cantidad[3] })
                    x= cantidad_fruta * lista_precio_fruta[3]
                    print(x)
                    tipo_de_pago()
                elif opcion == 5:
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar"))
                    print(cantidad_fruta + lista_cantidad[4])
                    x = cantidad_fruta * lista_precio_fruta[4]
                    print(x)
                    tipo_de_pago()
                elif opcion == 6:
                    carrito()
                elif opcion == 7:
                    print("salir")
                else:
                    print("no existe la fruta ")
        except Exception:
            print("invalida") 
    
def tipo_de_pago():
    for j in range (len(lista_pago)):
        print(f"{j + 1} {lista_pago[j]}")
    tipodepago=int(input("escoja una opcion :"))
    if tipodepago >= 1 and tipodepago <= 3:
        if tipodepago == 1:
            print("as escojido pagar con efectivo no hay descuento")
            
        elif tipodepago == 2:
            print("pagar con credito es un 15%. de descuento")
            resultado = (x / (100/15))
            print(resultado)
            resultadof=(x-resultado)
            print(f"total a pagar {resultadof}")
            

        elif tipodepago == 3:
            print("pagar con debito es un 10%. de descuento")
            resultado=x/ (100/15)
            print(resultado)
            resultadof=(x-resultado)
            print(f"toral a pagar{resultadof}")

        else:
            print("numero invalido")
    
    return(tipo_de_pago)

comprar()
