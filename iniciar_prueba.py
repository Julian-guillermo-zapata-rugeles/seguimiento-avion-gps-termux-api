import os
import json
import gps
import time

menu = """
#################################################
#                                               #
#   BIENVENIDO ! ESTE ES EL MÓDULO DE MANDO     #
#                                               #
#                                               #
#################################################

-> digite ok para iniciar la prueba
"""
TIME_ELAPSE_ERROR=5
TIME_ELAPSE = 0 # representa el tiempo en el que se intentará obtener posición gps
# recuerde que dependiendo de la ubicación y cobertura el sensor GPS  puede tardar más tiempo
# obtener los datos satelitales

print(menu)
iniciar=str(input(">> "))
if iniciar!="ok":
    exit()
registrador = gps.GpsTelemtry()
while True:
    status=registrador.get_telemetry()
    if status==True:
        registrador.get_information()
        registrador.save_information("telemetria.csv","latitude","longitude","altitude") # se guarda toda la información o se elige .
        time.sleep(TIME_ELAPSE)
    else:
        #------------------------------------------------------------------------------------
        print("Fallo en la obtención de datos --intentando en ",TIME_ELAPSE_ERROR,"segundos")
        time.sleep(TIME_ELAPSE_ERROR)
