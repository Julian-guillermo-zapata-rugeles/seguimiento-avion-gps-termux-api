import pandas as pd
import matplotlib.pyplot as plt
print("########### grafica altitud ############# ")
file_name = "telemetrias/"+str(input("Nombre archivo sin extencion : "))+".csv"
try:
    titulos = ["latitud","longitud","altitud","accuracy","vertical","bearing","speed","elapse","provider","time"]
    load_dataframe = pd.read_csv(file_name,delimiter=";")
    load_dataframe.columns = ["latitud","longitud","altitud","accuracy","vertical","bearing","speed","elapse","provider","time"]
    data_frame_altitud = load_dataframe["altitud"].str.replace("altitude:","").astype(float)
    prom = data_frame_altitud[0]
    counter = 0
    #data_frame_altitud.plot()
    for elements in data_frame_altitud:
        print(elements)
        prom = ( prom +  elements) // 2
        data_frame_altitud[counter]=prom
        counter=counter+1

    print(data_frame_altitud)
    plt.figure()
    data_frame_altitud.plot()
    plt.show()


except Exception as e:
    print("Error al abrir el archivo")
    print(e)
