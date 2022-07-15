lista_asignaturas=[]
menu2=["seleccione una opcion", "ver sus asignatura" , "quitar lista de asignatura","salir"]
def menu():
  for i in range (len(menu2)):
    print(f"{i + 1} {menu2[i]}")

def agregar():
    escribir=str(input("coloque las asignatura"))
    lista_asignaturas.append(escribir)
    print("__________________________")

def asignaturas():
    print(lista_asignaturas)

def quitar():
    try:
        print(lista_asignaturas)
        escribir=str(input("quitar asignatura"))
        lista_asignaturas.remove(escribir)
    except Exception:
        print("coloca algo")  

def opciones():
    while True:
            menu()
            opcion=int(input("ingrese una opcion:"))
            if opcion == 1:
                agregar()
            elif opcion == 2:
                asignaturas()
            elif opcion == 3:
                quitar()
            else:
                exit()
opciones()#codigo remasterisado
menu()
