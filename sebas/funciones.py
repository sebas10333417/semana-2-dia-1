viaje = []

def seleccionar_destino ():
    while True:
        tipo_viaje = input("""
        ==============================
        ==============================
        1. Internacional
        2. Nacional
        ==============================
        ==============================
        * Selecciona una opcion 1 o 2 * \n
        """)

        if tipo_viaje == 1: 
            print("="*30)
            print("!!! Viaje Internacional disponible !!! \n Medellin - España \n")
            print("!!! Fecha -> Septiembre 26 !!!: \n Hora -> 17:50 ")
            usuario = input("Quieres resevar este viaje? / si/no \n ")
            if usuario == "si":
                print("Tu viaje fue reservado con exito")
                viaje.append(usuario)
                print(viaje)
                continue
            else:
                print("="*30)
                break
                
            
        elif tipo_viaje == 2:
            print("="*30)
            print("!!! Viaje nacional disponible !!!  \n Medellin - Bogota ")
            print("!!! Fecha -> Octubre 29 !!! \n Hora -> 20:00 ")
            usuario2 = input("Quieres reservar este viaje? / si/no \n")
            if usuario2 == "si":
                print("Tu viaje fue reservado con exito")
                print("="*30)
                viaje.append(usuario2)
                print(viaje)
                continue
            else:
                print("="*30)
                break
                
            
def capacidad_viaje ():
    while True:
        carga = int(input("""
        !!Opciones de quipaje!! \n
        1. Equipaje de mano 
        2. Equipaje de bodega \n
        * Selecciona una opcion *
        
        """))
        
        if carga == 1:
            print("Equipaje de mano seleccionado, peso maximo 10kg: ")
            usuario3 = float(input("Ingresa el peso de tu equipaje \n "))
            if usuario3 > 13:
                print("Peso no aceptado")
            else:
                viaje.append(usuario3)
                print("Peso admitidido")
                break
        elif carga == 2:
            print("Equipaje de bodega seleccionado, peso maximo 50 kg")
            usuario4 = input("Ingresa el peso de tu equipaje \n ")
            if usuario4 > 50:
                print("Peso no aceptado")
            else:
                viaje.append(usuario4)
                print("Peso admitidido")
                break

def costo_viaje ():
    while True:
        costo = ("""
 """)
