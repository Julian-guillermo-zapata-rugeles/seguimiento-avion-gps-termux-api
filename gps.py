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

Ejemplo de respuesta de la API-TERMUX:
{
  "latitude": 5.95905344,
  "longitude": -75.73410794,
  "altitude": 1329.3951416015625,
  "accuracy": 34.30400085449219,
  "vertical_accuracy": 64.0,
  "bearing": 188.1999969482422,
  "speed": 0.699999988079071,
  "elapsedMs": 4,
  "provider": "gps"
}

###############################################################################################
"""
#------------------------------------ TEST DATA ---------------------------------------------#

local_test_data="""{
  "latitude": 6.95912344,
  "longitude": -73.73235794,
  "altitude": 1329.3951416015625,
  "accuracy": 34.30400085449219,
  "vertical_accuracy": 64.0,
  "bearing": 188.1999969482422,
  "speed": 0.699999988079071,
  "elapsedMs": 4,
  "provider": "gps"
}"""


import time
import os
import json

class GpsTelemtry():
    gps_information = {};

    def __init__( self, time_elapse , ):
        self.interval_test = time_elapse

    #----------------------------------------------------------------------------
    def get_telemetry(self):
        # Documentación para get_telemetry
        # Obtener mediante un llamado al sistema y a la API termux para obtener __string__ con la información de telemetria
        # convertir __string__ a diccionario usando la libreria json de python
        # almacenar durante el ciclo en self.gps_information
        try:
            tmp_raw_data_str = local_test_data # DEBUG: __string__ .
            #tmp_raw_data_str = os.popen('termux-location -p gps').read()

            # se espera que tmp_raw_data_str esté vacía si no se puede obtener telemetria del GPS
            # por tanto fallará la conversión a diccionario [Evitada]
            self.gps_information = json.loads(tmp_raw_data_str)
        except:
            # Error en __string__ tmp_raw_data_str  = "" ; [información al usuario]
            print("[Error GPS] : no se obtuvieron coordenadas GPS del dispositivo ")
        return None
    #----------------------------------------------------------------------------


    #----------------------------------------------------------------------------
    def get_information(self , *display_options ):
        # Documentación para get_information()
        # Usar el diccionario generado por get_telemetry para mostrar información genérica o personalizada
        # recibe como argumentos n __string__ para mostrar de forma personalizada
        # si la invocación del método es vacial , se muestran  todos los disponibles en el diccionario

        if len(display_options) == 0:
            try:
                print("Salida default (Completa)")
                for keys in self.gps_information.keys():
                    print("[OK]",keys)
            except:
                print("[Error Muestra] no hay datos gps en el diccionario")
        else:
            try:
                for args_display_options in display_options:
                    print("[Ok]",args_display_options , self.gps_information[args_display_options])
            except :
                print("[Error] datos no existentes en ",display_options);
                print("Disponible ------> ")
                for keys in self.gps_information.keys():
                    print(keys)
                return None



data=GpsTelemtry(1)
data.get_telemetry()
data.get_information()
