capacidad = 4
pila = [3]

while True:
    try:
        print("\n1, Agregar")
        print("2, sacar")
        print("3, salir")

        opcion = int(input("opcion: "))
        
        if opcion == 1:
            if len(pila) < capacidad:
                pila.append(input("dato: "))
            else:
                print("pila llena")

        elif opcion == 2:
            if pila:
                print("salio:", pila.pop())
            else:
                print("pila vacia")

        elif opcion == 3:
            break

    except:
        print("error")