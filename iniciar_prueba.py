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
TEST_SUCESS=0 # no const
TEST_FAILED=0 # no const -->
TIME_ELAPSE_ERROR=5
TIME_ELAPSE = 0 # representa el tiempo en el que se intentará obtener posición gps
# recuerde que dependiendo de la ubicación y cobertura el sensor GPS  puede tardar más tiempo
# obtener los datos satelitales

print(menu)
iniciar=str(input("continuar ? :"))
if iniciar!="ok":
    exit()
try:
    TIME_ELAPSE=float(input("tiempo entre pruebas : "))
except Exception as e:
    print("no es un numero válido para la prueba ")
    exit()
registrador = gps.GpsTelemtry()
while True:
    os.system("clear") # limpia la pantalla (consola)
    print("**********************************************************")
    print("Ejecutandose...\n")
    print("Tiempo tras error :",TIME_ELAPSE_ERROR)
    print("Tiempo sucessfull :",TIME_ELAPSE)
    print("Pruebas Exitosas : {}    -- Pruebas Fallidas : {}".format(TEST_SUCESS,TEST_FAILED))
    print("**********************************************************")
    status=registrador.get_telemetry()
    if status==True:
        registrador.get_information()
        registrador.save_information("telemetria.csv","latitude","longitude","altitude") # se guarda toda la información o se elige .
        TEST_SUCESS+=1
        time.sleep(TIME_ELAPSE)
    else:
        #------------------------------------------------------------------------------------
        print("Fallo en la obtención de datos --intentando en ",TIME_ELAPSE_ERROR,"segundos")
        time.sleep(TIME_ELAPSE_ERROR)
        TEST_FAILED+=1
