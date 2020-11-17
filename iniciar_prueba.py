import os
import json
import mod_gps.gps
import time
os.system("clear")
logo="""

 ██████████      ███                                █████                             █████
░░███░░░░░█     ░░░                                ░░███                             ░░███
 ░███  █ ░      █████  ██████   ██████  █████ ████ ███████    ██████   ████████    ███████   ██████
 ░██████       ░░███  ███░░███ ███░░███░░███ ░███ ░░░███░    ░░░░░███ ░░███░░███  ███░░███  ███░░███
 ░███░░█        ░███ ░███████ ░███ ░░░  ░███ ░███   ░███      ███████  ░███ ░███ ░███ ░███ ░███ ░███
 ░███ ░   █     ░███ ░███░░░  ░███  ███ ░███ ░███   ░███ ███ ███░░███  ░███ ░███ ░███ ░███ ░███ ░███
 ██████████     ░███ ░░██████ ░░██████  ░░████████  ░░█████ ░░████████ ████ █████░░████████░░██████
░░░░░░░░░░      ░███  ░░░░░░   ░░░░░░    ░░░░░░░░    ░░░░░   ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░  ░░░░░░
            ███ ░███
           ░░██████
            ░░░░░░
"""
menu = """
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
           Bienvenido al modulo de gestión

                 ██████╗██████╗███████╗
                ██╔════╝██╔══████╔════╝
                ██║  █████████╔███████╗
                ██║   ████╔═══╝╚════██║
                ╚██████╔██║    ███████║
                 ╚═════╝╚═╝    ╚══════╝

     Julian Guillermo Zapata Rugeles $no_kEy_mann$
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1) Iniciar Pruebas
2) Instrucciones Uso
3) Autor
4) Salir

"""

MENU_ITEMS  = ["1","2","3","4"]
# recuerde que dependiendo de la ubicación y cobertura el sensor GPS  puede tardar más tiempo
# obtener los datos satelitales


def iniciar_recoleccion():
    # Seleccion de tiempo
    global logo
    TEST_SUCESS=0 # no const
    TEST_FAILED=0 # no const -->
    TIME_ELAPSE_ERROR=0
    TIME_ELAPSE = 5 # representa el tiempo en el que se intentará obtener posición gps

    try:
        TIME_ELAPSE=float(input("Tiempo entre pruebas : "))
    except Exception as e:
        print("Por defecto {} segundos entre prueba".format(TIME_ELAPSE))

    #INICIO DEL PROGRAMA , SE CREA UN OBJETO DE GpsTelemtry
    registrador = mod_gps.gps.GpsTelemtry()

    while True:
        print(logo)
        print("**********************************************************")
        print("EJECUTANDOSE ...\n")
        print("INTERVALO TIEMPO :",TIME_ELAPSE,"SEGUNDOS\n")
        print("PRUEBAS EXITOSAS : {} <-> FALLIDAS {}".format(TEST_SUCESS,TEST_FAILED))
        print("**********************************************************")
        status=registrador.get_telemetry()
        if status==True:
            registrador.get_information()
            registrador.save_information("telemetria.csv") # se guarda toda la información o se elige .
            TEST_SUCESS+=1
            time.sleep(TIME_ELAPSE)
        else:
            #------------------------------------------------------------------------------------
            print("NO SE OBTUVO INFORMACIÓN DEL SATÉLITE")
            #time.sleep(TIME_ELAPSE_ERROR)
            TEST_FAILED+=1
        time.sleep(TIME_ELAPSE_ERROR)
        os.system("clear")
if __name__ == '__main__':
    while True:
        os.system("clear")
        print(menu)
        iniciar=str(input("Eleccion : "))
        if iniciar not in MENU_ITEMS:
            exit()
        if iniciar=="1":
            iniciar_recoleccion()
        elif iniciar=="2":
            os.system("clear")
            print(open("menu/m_instrucciones.txt").read())
