import time

jugadores = {"mateo": 126,
             "alex": 80,
             "sofia": 150,
             "lukas": 50,
             "nikola": 100,
             "tesla": 1000,
             "myteo": 125,
             "santiago": 150

}


def agregarpuntos(agregar):

    guardar = jugadores[usuario] + agregar
    print(f"Hemos agregado los puntos a tu nombre. Tienes {guardar} puntos")
    jugadores[usuario] = guardar


def quitarpuntos(quitar):
    
    quitar_puntos = jugadores[usuario] - quitar
    print(f"Has eliminado {quitar} puntos de tu nombre. Tienes {quitar_puntos} puntos restantes.")
    jugadores[usuario] = quitar_puntos
    

usuario = input("Escriba su nombre real:\n").lower()
if usuario.isalpha():
    if usuario in jugadores:
        menú = input(f"Tienes {jugadores[usuario]} puntos. Escriba uno de los siguientes métodos agregar/quitar:\n").lower()
        time.sleep(1)
        if menú.isalpha():
            if menú == "agregar":
                agregar = input("Escriba el monto que desee agregar:\n")
                if agregar.isdigit():

                    agregar = int(agregar)

                    agregarpuntos(agregar)
                else:
                    print("Escriba el monto que desea agregar en cifras.")
            elif menú == "quitar":
                quitar = input("Escriba el monto que desee quitar:\n")
                if quitar.isdigit():
                    
                    quitar = int(quitar)

                    if quitar <= jugadores[usuario]:

                        quitarpuntos(quitar)
                    else:
                        print("La cifra que quieres quitar excede de tu saldo total.")
                else:
                    print("Escriba el monto que desea quitar en cifras.")
            else:
                print("Escriba uno de los métodos dados nuevamente.")
        else:
            print("Escriba el  método nuevamente.")
    else:
        print("Usuario no encontrado. inténtelo de nuevo.")          
else:
    print("Escriba su nombre real.")