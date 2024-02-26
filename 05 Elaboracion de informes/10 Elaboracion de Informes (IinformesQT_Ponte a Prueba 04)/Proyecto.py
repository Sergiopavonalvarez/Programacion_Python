import os
import pandas as pd
import datapane as dp

#fichero_csv = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)"
fichero_csv="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)/"
os.chdir(fichero_csv)
fichero_csvv = "2024.02.24_1-1.csv"
df = pd.read_csv(fichero_csvv)
dp.enable_logging()


print(df.columns)
titulo = dp.HTML("<h1 style='text-align:center; color:#4CAF50;'>Informe: Marte 2021</h1>")

media_temperatura = df[' Temperatura_[ºC]'].mean()
media_presion = df['Presion_[Pa]'].mean()
media_altitud = df['Altitud_[m]'].mean()
nombres_equipo = df['Equipo'].unique()



unidades_temperatura = dp.BigNumber(heading='Temperatura media', value=media_temperatura, )
unidades_presion = dp.BigNumber(heading='Presion media', value=media_presion, )
unidades_altitud = dp.BigNumber(heading='Altitud media', value=media_altitud, )
nombre = dp.BigNumber(heading='Equipo', value=nombres_equipo[0], )

fichero=dp.Attachment(file='/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)/2024.02.24_1-1.csv', filename='Proyecto Marte.csv')
#fichero = dp.Attachment(file='C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)/2024.02.24_1-1.csv',filename='Proyecto Marte.csv')
texto = dp.Text('**Puedes descargar el fichero con los datos del informe:**')
#report = dp.Report(titulo, unidades_temperatura, unidades_presion, unidades_altitud, nombre,texto, fichero)

report = dp.Report(
    dp.Page(
        title='Informe',
        blocks=[titulo, unidades_temperatura, unidades_presion, unidades_altitud, nombre, texto, fichero]
    ),
    dp.Page(
        title='Graficos',
        blocks=[dp.Text("Añade tus gráficos aquí.")]
    ),
    dp.Page(
        title='No se',
        blocks=[dp.Text("Añade contenido aquí.")]
    )
)




report.save(path="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)/Proyecto Marte.html", open=True)
#report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)/Proyecto Marte.html",open=True)
