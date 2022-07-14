carrito=[]


lista_fruta=["manzana", "platano","uva","mandarina","cacao","carrito de compra"," salir"]
lista_precio_fruta=[1000,2000,5000,7000,10000]
lista_cantidad=[0,0,0,0,0]
lista_pago=["pagar con efectivo","pagar con credito", "pagar con debito"]

def mostrarmenu():
    for i in range (len(lista_fruta)):
        print(f"{i+1} {lista_fruta[i]}")

def comprar():
    while True:
        try:
            global x
            mostrarmenu()
            print("_______________________________________________________________")
            opcion=int(input("escoje una opcion:"))
            print("_____________________________________________________________-")
            if opcion >= 1 and opcion <= 7:
                print(f"escojistes la opcion {lista_fruta[opcion-1]}")
                if opcion == 1 :
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar:"))
                    print(f"{cantidad_fruta + lista_cantidad[0]}")
                    x=cantidad_fruta * lista_precio_fruta[3]
                    lista_cantidad[0] += cantidad_fruta
                    x=cantidad_fruta * lista_precio_fruta[0]
                    print(f"{x} {lista_fruta[0]}")
                    tipo_de_pago(lista_fruta[0])
                    carrito.append(lista_fruta[0])
                elif opcion == 2:
                    cantidad_fruta= int(input("ingrese la cantidad de fruta que desea llevar:"))
                    print(f"{cantidad_fruta + lista_cantidad[1]}")
                    x=cantidad_fruta * lista_precio_fruta[1]
                    lista_cantidad[1] += cantidad_fruta
                    x=cantidad_fruta * lista_precio_fruta[1]
                    print(f"{x} {lista_fruta[1]}")
                    tipo_de_pago(lista_fruta[1])
                    carrito.append(lista_fruta[1])
                elif opcion == 3:
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar:"))
                    print({cantidad_fruta + lista_cantidad[2]})
                    x=cantidad_fruta * lista_precio_fruta[2]
                    lista_cantidad[2] += cantidad_fruta
                    x=cantidad_fruta * lista_precio_fruta[2]
                    print(f"{x} {lista_fruta[2]}")
                    tipo_de_pago(lista_fruta[2])
                    carrito.append(lista_fruta[2])
                elif opcion == 4:
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar:"))
                    print({cantidad_fruta + lista_cantidad[3] })
                    x= cantidad_fruta * lista_precio_fruta[3]
                    lista_cantidad[3] += cantidad_fruta
                    x=cantidad_fruta * lista_precio_fruta[3]
                    print(f"{x} {lista_fruta[3]}")
                    tipo_de_pago(lista_fruta[3])
                    carrito.append(lista_fruta[3])

                elif opcion == 5:
                    cantidad_fruta =int(input("ingrese la cantidad de fruta que desea llevar:"))
                    print(cantidad_fruta + lista_cantidad[4])
                    x = cantidad_fruta * lista_precio_fruta[4]
                    lista_cantidad[4] += cantidad_fruta
                    x=cantidad_fruta * lista_precio_fruta[4]
                    print(f"{x} {lista_fruta[4]}")
                    tipo_de_pago(lista_fruta[4])
                    carrito.append(lista_fruta[4])
                elif opcion == 6:
                    carrito_ver()
                elif opcion == 7:
                    print("salir")
                else:
                    print("no existe la fruta ")
        except Exception:
            print()
    
def tipo_de_pago(fruta):
    global resultadof
    for j in range (len(lista_pago)):
        print(f"{j + 1} {lista_pago[j]}")

    tipodepago=int(input("escoja una opcion :"))
    if tipodepago >= 1 and tipodepago <= 3:
        if tipodepago == 1:
            print("as escojido pagar con efectivo no hay descuento")
            print("________________________________________________________________")
            resultadof=resultado-0
            print(f"total a pagar {resultadof}")
            
            

        elif tipodepago == 2:
            print("pagar con credito es un 15%. de descuento")
            resultado = (x / (100/15))
            print(resultado)
            resultadof=(x-resultado)
            print(f"total a pagar {resultadof}")
            print("______________________________________________________________")


        elif tipodepago == 3:
            print("pagar con debito es un 10%. de descuento")
            resultado=x/ (100/15)
            print(resultado)
            resultadof=(x-resultado)
            print(f"total a pagar{resultadof}")
            print("_____________________________________________")

        else:
            print("numero invalido")
    
    return(tipo_de_pago)

def carrito_ver():
   carrito.append(resultadof)
   print(carrito)
comprar()
