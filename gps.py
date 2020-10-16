"""
##############################################################################################
                            PRUEBA SENCILLA DE TELEMETRIA GPS
                       Desarollado por Julian Guillermo Zapata Rugeles

Objetivo :
    Usar la api termux disponible para android y python3 para obtener periodicamente
    datos del sensor GPS presente dispositivos de tipo android y generar un archivo
    que contenga telemetria.
    se ejecutará una instancia de termux-api llamada termux-location que acepta las siguientes
    banderas.
        -p provider gps [network, gps , ...]
        -r nonce , last ...
        termux-location -h para más información
    Se usará para obtener coordenadas GPS y trazar la trayectoria de un avión en periodos T
    la telemetria se usará para trazar la ruta empleada.
    -- telemetria sobre viajes terrestres
    -- para obtener coordenadas en un momento x.

    # USO FUTURO :
        --Generar alertas cuando se encuentre a un radio determinado de coordenadas dadas.
        --Intentar conectarla con una API personal.

###############################################################################################
"""
import time
import os
import json

class GpsTelemtry():
    gps_information = [];

    def __init__():
