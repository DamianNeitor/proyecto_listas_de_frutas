#Ejercicio 10
#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en 
# función de su respuesta le muestre un menú con los ingredientes disponibles para que 
# elija.
#  Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en 
# todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana
#  o no y todos los ingredientes que lleva.

lista=["vegetariano" ,"no vegetariano"]
ingredientes2=["pimiento","tofu"]
ingredientes3=["peperoni" ,"jamon","salmon"]
def menu ():
    for i in range (len(lista)):
        print(f"{i+1} {lista[i]}")
        
def vegetariano():
    print("````vegetariano```")  
    print("____________________________")  
    for i in range (len(ingredientes2)):
        print(f"{i+1} {ingredientes2[i]}")
    print("________________________________________________________")
    ingredientes=int(input("ingrese el ingrediente:"))
    print("________________________________________________________")
    if ingredientes == 1:
        print(*{ingredientes2[0]})
        pagarpimiento()
    else:
        print(*{ingredientes2[1]})
        totalpagartofu()
        
def Novegetariano():
    print("^^^^^^^^^^^^^ No vegetariana ^^^^^^^^^^^^^^")
    print("_________________________________________________")
    for i in range (len(ingredientes3)):
        print(f"{i+1} {ingredientes3[i]}")
    print("________________________________________________________")
    opcion = input("ingrese una opcion:")
    print("________________________________________________________")
    if opcion == 1:
        print(f"as escojido {ingredientes3[0]}")
        peperoni()
    elif opcion == 2:
        print(f"as escojido {ingredientes3[1]}")
        jamon()
    else:
        print(f"as escojido {ingredientes3[2]}")  
        salmon()
    
def pagarpimiento():
    escojer=input("desea agregar un refresco ? si /no:")
    if escojer == "si":
        refresco()
    elif  escojer == "no":
        opciones()   
        
def totalpagartofu():
    total=int(input("la pizza con pimiento vale 5000 ingrese la cantidad que deas pagar: "))
    print(F" su vuelto es {total-5000}")
    
    escojer=input("desea agregar un refresco ? si /no:")
    if escojer == "si":
        refresco()
    elif  escojer == "no":
        opciones()   
    
def peperoni():
    total=int(input("la pizza con pimiento vale 5000 ingrese la cantidad que deas pagar: "))
    print(F"su vuelto es {total-3500}")
    escojer=input("desea agregar un refresco ? si /no:")
    if escojer == "si":
        refresco()
    elif  escojer == "no":
        opciones()   
    
def jamon(total):
    total=int(input("la pizza con pimiento vale 5000 ingrese la cantidad que deas pagar: "))
    print(F" su vuelto es {total-3500}")  
    
    escojer=input("desea agregar un refresco ? si /no:")
    if escojer == "si":
        refresco()
    elif  escojer == "no":
        opciones()   
        
def salmon():
    total=int(input("la pizza con pimiento vale 5000 ingrese la cantidad que deas pagar:"))
    print(F"su vuelto es  {total-3500}")  
    
    escojer=input("desea agregar un refresco ? si /no:")
    if escojer == "si":
        refresco()
    elif  escojer == "no":
        opciones()       
        
def refresco():
    print("todas las bebidas salen 1000")
    print("1)coca cola")
    print("2)pepsi")
    print("3)sprit")
    print("4)jugo de naranja")
    print("5)cafe")
    refrescoger=int(input("con cuanto desea pagar?"))
    escribir=input("escribi el refresco que quieres: ")
    print(f"su refresco a elegir es {escribir} y su vuelto es = { refrescoger - 1000} ")
    opciones()
        
def opciones():
    print("__________________________________________________________________")
    menu()
    sino=int(input("si que sea vegetariana opcion 1 y no opcion /2 :?: "))
    print("___________________________________________________________________")    
    if sino == 1:
        vegetariano()
    elif sino == 2:
        Novegetariano()
    else:
        print()
     
opciones()
