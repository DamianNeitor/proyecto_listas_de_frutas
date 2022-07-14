guardado=[]
menu=["anotar" ,"ver los pedidos","quitar pedidos" , "salir"] #menu
def menu1():
    for i in range(len(menu)):
        print(f"{ i+1 } {menu[i]}]")
        

def guardado1():
    print(f"recordatorio {(guardado)}")
    print(guardado)
        

def mein():
    while True:
        menu1()
        print("____________")
        ver=str(input("escoja una opcion:"))
        print("____________")
        print("_____________________________")
        if ver == "1":
            escribir=str(input("deme los productos a encargar:"))
            guardado.append(escribir)
        elif ver == "2":
            guardado1()
        elif ver == "3":    
            print(guardado)
            escribir=str(input("deme los productos que desea quitar:"))
            guardado.remove(escribir)
            print( f"{(guardado)} ")
            
        else: 
            exit()

mein()
