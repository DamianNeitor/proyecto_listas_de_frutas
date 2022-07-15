guardado=[]
menu=["anotar" ,"ver los pedidos","quitar pedidos" , "salir"] #menu
def menu1():
    for i in range(len(menu)):
        print(f"{ i+1 } {menu[i]}]")
        

def guardado1():
    print(f"recordatorio {(guardado)}")

        

def mein():
    while True:
        try:   
            menu1()
            print("_____________________________")
            ver=int(input("escoja una opcion:"))
            print("_____________________________")
            if ver == 1:
                escribir=str(input("deme los productos a encargar:"))
                guardado.append(escribir)#agregar con el mismo objeto de la variable
            elif ver == 2:
                guardado1()#llamos a la funcion guardado cual imprime
            elif ver == 3:    
                print(guardado)
                escribir=str(input("deme los productos que desea quitar:"))
                guardado.remove(escribir)#remover los objetos con el mismo valor de variable
                print( f"{(guardado)} ")
            else: 
                exit()
        except Exception:
            print("porfavor ingrese algo")#el error es cuando no hay nada en el inventario
mein()
#recordatorio no meter string a menos que sea necesario asi con el try se arregla el error de todo por si cometes un fallo de apretar una tecla
