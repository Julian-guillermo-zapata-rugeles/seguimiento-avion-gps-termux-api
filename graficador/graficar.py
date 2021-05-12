"""
        Desarollado por Julian Guillermo Zapata Rugeles 2020
                        licencia GPL V3
                    Licencia pública de GNU

Este código puede ser modificado , compartido y distribuido bajo
la licencia publica de Gnu v3, las librias aquí inscritas pueden
  contener derechos, es conveniente revisar licencia folium
 cualquier alusión a folium y agradecimientos a sus creadores.

El script fue realizado por Julian Guillermo Zapata Rugeles y NO
es necesario autorización previa para su uso. solo distribuyelo
            bajo software libre utíl para todos.

Este script utiliza la librería folium para graficar puntos en mapa
los datos previamente exportados corresponden a latitud y longitud
del script gps.

para instalar la librería folium use:
        sudo pip3 install folium (gnu/linux)

llamado a set_point    50,  [5.95971778,-75.73417013] , "Blue" , False
                      radio         coordenadas          color   relleno

radio = se generará un color_circulo de radio 50 (o el numero que se le pase )
        en base a las coordenadas latitud y longitud dadas.

coordenadas = [latitud,longitud] debe ser una lista
color = establece el color del color_circulo generado con radio -> radio en color RGB #HTML
relleno = False o True para relleno
"""

import os

#MODO="Stamen Toner"   # descomenta algunos de los dos paa genrar el mapa
MODO="Stamen Terrain"  # ... ...  ... ... ... ... .... ... ... ... ... ...


try:
    import folium
except Exception as e:
    print("folium no se encuentra instalado :")
    print("Ejecuta en pip3 :")
    print("sudo pip3 install folium (gnu/linux)")
    exit()


try:
    file_name=open(input("Nombre Archivo csv: ")).read().split('\n')
    iterator=0
    try:
        for telemetria in range(len(file_name)-1):
            sub_string=file_name[telemetria]
            sub_list=sub_string.split(';')
            latitud_raw  = sub_list[0]
            longitud_raw = sub_list[1]
            clear_latitud= latitud_raw.replace("latitude:","")
            clear_longitud =longitud_raw.replace("longitude:","")
            if iterator==0:
                m=folium.Map(
                location=[float(clear_latitud),float(clear_longitud)],
                tiles=MODO, # modo por defecto
                zoom_start=10 )
                iterator=iterator+1
                print("Mapa creado desde coordenadas GPS")
            else:
                print("añadiendo punto ",clear_latitud,clear_longitud)
                folium.Circle(
                    radius=2,
                    location=[float(clear_latitud),float(clear_longitud)],
                    popup=str(iterator),
                    color="red",
                    fill=True,
                    fill_color="red"
                    ).add_to(m)
                iterator+=1
        m.save("index.html")
    except Exception as e:
        print(e)
except Exception as e:
    print("Detalles del error : ",e)
    exit()
