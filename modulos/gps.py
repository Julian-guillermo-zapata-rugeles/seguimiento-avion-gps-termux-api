"""
--------------------------------------------------------------------------------------------------------
                                     TELEMETRIA GPS
                       Desarollado por Julian Guillermo Zapata Rugeles
                                      GPL LICENSE V3

                         Author : Julian Guillermo Zapata Rugeles
                                         2020
                Python 3.7.3 (default, Jul 25 2020, 13:03:44) GNU/LINUX
                 Android 10 - termux api -- termux shell -- LINUX/Generic


Puedes tomar,editar,compartir este código y distribuirlo bajo licencia de software libre unicamente.
https://www.gnu.org/licenses/gpl-3.0.txt (para más información)


OBJETIVO  :
    Usar la api termux disponible para android y python3 para obtener periodicamente
    datos del sensor GPS presente dispositivos de tipo android y generar un archivo
    que contenga telemetria.
    -se procesará y almacenará en texto plano con formato tipo csv
    -se puede almacenar en tipo json estandar para post procesamiento
    se ejecutará una instancia de termux-api llamada termux-location que acepta las siguientes
    banderas.
        -p provider gps [network, gps..]
        -r nonce , last ...
        termux-location -h para más información
    Se usará para obtener coordenadas GPS y trazar la trayectoria de un avión en periodos T
    la telemetria se usará para trazar la ruta empleada.
    -- telemetria sobre viajes terrestres
    -- para obtener coordenadas en un momento x.
    --graficar a travéz de follium un mapa basado en open street que contiene datos de telemetria

INSTRUCCIONES DE USO:

    1)
        Este script funciona exclusivamente en un entorno termux en dispositivos Android
        para su uso se debe instalar a travez de la tienda de aplicaciones
        TERMUX
        TERMUX - API

    2)
        Una vez suplido estos requisitos de debe instalar python3 en el entorno
        esto se logra usando el siguiente comando : pkg install python3
                                                    pkg install git

    3)
        Se realizará un git clone del repositorio ó lleve estos archivos al entorno termux
        Ejecute iniciar prueba y listo.
        Recuerde permitir el uso del sensor GPS para la prueba.
        -- al obtener resultados puede graficarlos usando graficador.py


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
-------------------------------------------------------------------------------------------------------- """



#------------------------------------ TEST DATA ---------------------------------------------#
# para usar los datos de prueba dirijasé al método get_telemetry y active la linea
# # DEBUG:  que contienen la información de local_test_data presente a continuación.

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

    def __init__( self ):
        pass
    #----------------------------------------------------------------------------
    def get_telemetry(self):
        # Documentación para get_telemetry
        # Obtener mediante un llamado al sistema y a la API termux para obtener __string__ con la información de telemetria
        # convertir __string__ a diccionario usando la libreria json de python
        # almacenar durante el ciclo en self.gps_information
        try:
            #------------------------------------------------------------------------------------
            # LINEAS PARA COMPROBACIÓN DE EJECUCIÓN CORRECTA DEL PROGRAMA
            #

            # XXXXXXXXXXXXXXXXXXXXXXX MODO DE PRUEBAS XXXXXXXXXXXXXXXXXXXXXXXXXX
            #tmp_raw_data_str = local_test_data # DEBUG: __string__ . DESCOMENTAR PARA USAR VALOR PRUEBA
            tmp_raw_data_str = os.popen('termux-location -p gps').read() # COMENTAR PARA USO REAL


            # FIN LINEAS DE PRUEBA Y DEPURACIÓN
            #------------------------------------------------------------------------------------

            # se espera que tmp_raw_data_str esté vacía si no se puede obtener telemetria del GPS
            # por tanto fallará la conversión a diccionario [Evitada]
            self.gps_information = json.loads(tmp_raw_data_str)
        except:
            # Error en __string__ tmp_raw_data_str  = "" ; [información al usuario]
            print("[Error GPS] : no se obtuvieron coordenadas GPS del dispositivo ")
            return False
        return True
    #----------------------------------------------------------------------------




    #----------------------------------------------------------------------------
    def get_information(self , *display_options ):
        # Documentación para get_information()
        # Usar el diccionario generado por get_telemetry para mostrar información genérica o personalizada
        # recibe como argumentos n __string__ para mostrar de forma personalizada
        # si la invocación del método es vacial , se muestran  todos los disponibles en el diccionario

        if len(display_options) == 0:
            try:
                # mostrar todos los valores telemetria disponibles y almacenados en self.gps_information
                # si display_options no tiene argumentos se muestra por default todos
                print("Salida default (Completa)")
                for keys in self.gps_information.keys():
                    print("[OK]",keys,self.gps_information[keys])  # se muestra las claves y sus valores
            except:
                print("[Error Muestra] no hay datos gps en el diccionario")
                # si ocurrió algún error anteriormente en la obtención de datos este paso fallará pero será manejado.
        else:
            try:
                for args_display_options in display_options:
                    # de recibir agumentos en *display_options con args ** () tuple.
                    print("[Ok]",args_display_options , self.gps_information[args_display_options])
                    #se imprime únicamente esos valores deseados.
            except :
                print("[Error] datos no existentes en ",display_options); # si en *display_options no keys in self.gps_information
                print("*******************   disponible *******************")
                #se muestra las claves permitidas para el diccionario, para ser pasadas nuevamente
                for keys in self.gps_information.keys():
                    print(keys)
                return None
    #----------------------------------------------------------------------------


    def save_information(self,file_name="dataset.csv",*display_options):
        # esta función guardará los datos de forma texto o según especificación.
        # recibe dos argumentos, nombre de archivo y una lista *args de datos a exportar

        try:
            ostream_data=open(file_name,'a')
        except Exception as e:
            print("[Error] Al generar el archivo , verifique si posee permisos de escritura en disco.")
        if len(display_options)==0:
            print("[Default] almacenamiento")
            print("[Default] guardar")
            for keys in self.gps_information.keys():
                ostream_data.write(keys)
                ostream_data.write(":")
                ostream_data.write(str(self.gps_information[keys]))
                ostream_data.write(";")
            lt = time.localtime() # return tuple with local time phone
            ostream_data.write(str(lt[0:5])) # asociamos fecha al registro a escribir
            ostream_data.write("\n")
            ostream_data.close()
        else:
            print("[Personalizado] guardar")
            for keys in display_options:
                try:

                    ostream_data.write(keys)
                    ostream_data.write(":")
                    ostream_data.write(str(self.gps_information[keys]))
                    ostream_data.write(";")
                except:
                    pass
            lt = time.localtime() # return tuple with local time phone
            ostream_data.write(str(lt[0:5])) # asociamos fecha al registro a escribir
            ostream_data.write("\n")
            ostream_data.close()
        return  None
