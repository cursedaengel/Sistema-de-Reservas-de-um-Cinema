A1 = A2 = A3 = A4 = A5 = True
arrendador1 = arrendador2 = arrendador3 = arrendador4 = arrendador5 = ">>ASIENTO LIBRE<<"
contador = 0

def poltrona():
    eleccion_poltrona = input("\nElija una poltrona disponible (A1, A2, A3, A4, A5): ").upper()
    return eleccion_poltrona

def nombre():
    nombre_arrendador = input("\nIngrese el nombre del arrendador: ")
    return nombre_arrendador

def reservas():
    global A1, A2, A3, A4, A5
    global arrendador1, arrendador2, arrendador3, arrendador4, arrendador5
    
    eleccion = poltrona()
    
    if eleccion == "A1":
         if A1:
            arrendador1 = nombre()
            print("¡Reserva completada! Poltrona: A1 / Nombre: {}".format(arrendador1))
            A1 = False
            return True
         else:
            print("La poltrona ya ha sido reservada por {}".format(arrendador1))
         
    elif eleccion == "A2":
        if A2:
            arrendador2 = nombre()
            print("¡Reserva completada! Poltrona: A2 / Nombre: {}".format(arrendador2))
            A2 = False
            return True
        else:
            print("La poltrona ya ha sido reservada por {}".format(arrendador2))

    elif eleccion == "A3":
        if A3:
            arrendador3 = nombre()
            print("¡Reserva completada! Poltrona: A3 / Nombre: {}".format(arrendador3))
            A3 = False
            return True
        else:
            print("La poltrona ya ha sido reservada por {}".format(arrendador3))
        
    elif eleccion == "A4":
        if A4:
            arrendador4 = nombre()
            print("¡Reserva completada! Poltrona: A4 / Nombre: {}".format(arrendador4))
            A4 = False
            return True
        else:
            print("La poltrona ya ha sido reservada por {}".format(arrendador4))

    elif eleccion == "A5":
        if A5:
            arrendador5 = nombre()
            print("¡Reserva completada! Poltrona: A5 / Nombre: {}".format(arrendador5))
            A5 = False
            return True
        else:
            print("La poltrona ya ha sido reservada por {}".format(arrendador5))


    else:
        print("Poltrona inválida")
    
def menu():
    global contador
    global arrendador1, arrendador2, arrendador3, arrendador4, arrendador5

    while True:
        print("\n•♡•♡•♡•♡ Este es el menú principal ♡•♡•♡•♡•♡•\nIngrese el número de la opción deseada para usar el sistema:\n[1] para >>VER CATALOGO DE PELÍCULAS<<\n[2] para >>RESERVAS<<\n[3] para >>CANCELAR RESERVA<<\n[4] para >>VER DISPONIBILIDAD DEL CINE<<\n[5] para >>SALIR<<")
        eleccion_menu = int(input("\nPara navegar por la aplicación, elija una opción abajo.\n¿En qué puedo ayudarte? "))

        if eleccion_menu == 1:
                print("\nEste es el >>CATÁLOGO DE PELÍCULAS<<\n\n1. Los DOMINGOS, el cine transmite: >>ANATOMÍA DE UNA CAÍDA<<\nGénero: Crimen/Thriller\nSinopsis: Durante el último año, Sandra, una escritora alemana, y Samuel, su marido francés, vivieron juntos con Daniel, el hijo de 11 años de la pareja, en una pequeña y aislada ciudad en los Alpes. Cuando Samuel es encontrado muerto, la policía trata el caso como un posible homicidio, y Sandra se convierte en la principal sospechosa.\n\n2. Los LUNES, el cine transmite: >>OLDBOY<< \nGénero: Thriller/Acción \nSinopsis: Dae-Su es secuestrado y mantenido cautivo por 15 años en una habitación de hotel, sin contacto con el mundo exterior. Cuando es liberado inexplicablemente, descubre que está acusado de asesinar a su esposa y emprende una misión obsesiva de venganza.\n\n3. Los MARTES, el cine transmite: >>EL NIÑO Y LA GARZA<< \nGénero: Fantasía/Aventura \nSinopsis: Mahito, un niño de 12 años, lucha por establecerse en una nueva ciudad después de la muerte de su madre. Cuando una garza hablante le dice que su madre sigue viva, entra en una torre abandonada en su búsqueda, lo que lo lleva a otro mundo.\n\n4. Los MIÉRCOLES, el cine transmite: >>MULHERES ADORÁVEIS<<\nGénero: Romance/Drama\nSinopsis: En los años posteriores a la Guerra de Secesión, Jo March y sus dos hermanas regresan a casa cuando Beth, la tímida hermana menor, desarrolla una enfermedad devastadora que cambia sus vidas para siempre.\n\n5. Los JUEVES, el cine transmite: >>DUNA<<\nGénero: Ciencia ficción/Aventura\nSinopsis: Paul Atreides es un joven brillante, dueño de un destino más allá de su comprensión. Debe viajar al planeta más peligroso del universo para asegurar el futuro de su pueblo.\n\n6. Los VIERNES, el cine transmite: >>HASTA EL ÚLTIMO HOMBRE<<\nGénero: Guerra/Drama \nSinopsis: Siga la historia de Desmond T. Doss, un médico del ejército estadounidense que, durante la Segunda Guerra Mundial, se niega a usar armas. Durante la Batalla de Okinawa, trabaja en la sala médica y salva a cerca de 75 hombres.\n\n7. Los SÁBADOS, el cine transmite: >>LA SOCIEDAD DE LA NIEVE<<\nGénero: Aventura/Thriller\nSinopsis: En 1972, un vuelo desde Uruguay choca con un glaciar en los Andes. Solo 29 de los 45 pasajeros sobrevivieron al accidente. Atrapados en uno de los ambientes más hostiles del planeta, se ven obligados a luchar por sus vidas.")

        elif eleccion_menu == 2:
            if contador < 5:
                personas = int(input("\nIniciaremos el proceso. ¿Cuántos asientos deseas reservar? Recuerda que la capacidad máxima del cine es >>5 ASIENTOS<<: "))
                if contador + personas > 5:
                    print("El número de personas excede la capacidad máxima. Puedes reservar para hasta {} personas.".format(5 - contador))
                else:
                    reservas_necesarias = personas

                    while reservas_necesarias > 0:
                        if reservas():
                            contador += 1
                            reservas_necesarias -= 1
            else:
                    print("\n>>>>>>>CINE LLENO.<<<<<<<< \n No hay asientos disponibles.") 
            
        elif eleccion_menu == 3:
            cancelamento()

        elif eleccion_menu == 4:
            print("\n•♡•♡•♡•♡ Disponibilidad de los asientos: \nA1 está con {}\nA2 está con {}\nA3 está con {}\nA4 está con {}\nA5 está con {}".format(arrendador1, arrendador2, arrendador3, arrendador4, arrendador5))
            
        elif eleccion_menu > 4:
            print("\n¡Gracias por usar el sistema! \n>>CERRANDO LA APLICACIÓN...<<")
            return False


def cancelamento():
    global A1, A2, A3, A4, A5
    global arrendador1, arrendador2, arrendador3, arrendador4, arrendador5
    global contador
    
    cancelamento = input("¿Deseas cancelar la reserva de qué asiento? ").upper()
    
    if cancelamento == "A1":
        if not A1:
            arrendador1 = ">>ASIENTO LIBRE<<"
            contador -= 1
            print("Cancelación del asiento A1 completada.")
            A1 = True
            return True 
        else:
            print("No hay reservas en este asiento.")
    
    if cancelamento == "A2":
        if not A2:
            arrendador2 = ">>ASIENTO LIBRE<<"
            contador -= 1
            print("Cancelación del asiento A2 completada.")
            A2 = True
            return True
        else:
            print("No hay reservas en este asiento.")
    
    if cancelamento == "A3":
        if not A3:
            arrendador3 = ">>ASIENTO LIBRE<<"
            contador -= 1
            print("Cancelación del asiento A3 completada.")
            A3 = True
            return True 
        else:
            print("No hay reservas en este asiento.")
    
    if cancelamento == "A4":
        if not A4:
            arrendador4 = ">>ASIENTO LIBRE<<"
            contador -= 1
            print("Cancelación del asiento A4 completada.")
            A4 = True
            return True 
        else:
            print("No hay reservas en este asiento.")
    
    if cancelamento == "A5":
        if not A5:
            arrendador5 = ">>ASIENTO LIBRE<<"
            contador -= 1
            print("Cancelación del asiento A5 completada.")
            A5 = True
            return True 
        else:
            print("No hay reservas en este asiento.")
  
import time
import sys

def intro():
    
    def bienvenida(mensaje):
        for char in mensaje:
            time.sleep(0.05)
            print(char, end='', flush=True)
        print()

    def mostrar_carregamento():
        print("\nIniciando el sistema...")
        barra = "[                    ]"
        for i in range(20): 
            time.sleep(0.2)
            barra = "".join("█" if j == i else " " for j in range(20))
            porcentaje = (i + 1) * 5
            sys.stdout.write(f"\r{barra} {porcentaje}%")
            sys.stdout.flush()
        print("\n")

    def cine_ascii():
        cine = """
        ██████╗██╗███╗   ██╗███████╗███╗   ███╗ █████╗ 
        ██╔════╝██║████╗  ██║██╔════╝████╗ ████║██╔══██╗
        ██║     ██║██╔██╗ ██║█████╗  ██╔████╔██║███████║
        ██║     ██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══██║
        ╚██████╗██║██║ ╚████║███████╗██║ ╚═╝ ██║██║  ██║
        ╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝
        """
        print(cine)

    mostrar_carregamento()
    cine_ascii()
    bienvenida("¡Bienvenido al cine! Prepárate para una experiencia increíble y disfruta de tu película.")

intro()

menu()
