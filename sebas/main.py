from funciones import *

while True:
    print("!!! Menu gestio de viaje !!!")
    print("--------------------")
    print("--------------------")
    lista_menu = int(input("""
    1. Seleccionar destino
    2. Seleccionar capacidad de equipaje
    3. Costo del viaje
    4. Comprar boleto
    5. Imprimir boleto
    6. salir

    !! Por favor ingresa una opcion segun la eleccion del 1 al 6 !!
    """))
    while True:
        if lista_menu == 1:
            seleccionar_destino()

        if lista_menu == 2:
            capacidad_viaje()
        if lista_menu == 3:
            costo_viaje()
        if lista_menu == 4:
            comprar_boleto()
        if lista_menu == 5:
            imprimir_boleto()
        if lista_menu == 6:
            salir()
        break