import os
import pandas as pd
import datapane as dp

fichero_csv = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/10 Elaboracion de Informes (Proyecto Completo)"
#fichero_csv="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (Proyecto Completo)/"
ruta_imagen= "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/10 Elaboracion de Informes (Proyecto Completo)/logo.jpg"
dp.Media(ruta_imagen)
os.chdir(fichero_csv)
fichero_csvv = "2024.02.24_1-1.csv"
df = pd.read_csv(fichero_csvv)
dp.enable_logging()

print(df.columns)
titulo = dp.HTML("<h1 style='text-align:center; color:#4CAF50;'>Informe: Marte 2021</h1>")
titulo2 = dp.HTML("<h1 style='text-align:center; color:#4CAF50;'>Grafico: Marte 2021</h1>")
titulo3 = dp.HTML("<h1 style='text-align:center; color:#4CAF50;'>Datos: Marte 2021</h1>")

table=dp.Table(df)
data_table=dp.DataTable(df)

media_temperatura = df[' Temperatura_[ºC]'].mean()
media_presion = df['Presion_[Pa]'].mean()
media_altitud = df['Altitud_[m]'].mean()
nombres_equipo = df['Equipo'].unique()

ventas_mes = df.groupby(['Paquete'], sort=False).sum()
grafico_matplot_lineas = ventas_mes.plot(y=' Temperatura_[ºC]')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

unidades_temperatura = dp.BigNumber(heading='Temperatura media', value=media_temperatura, )
unidades_presion = dp.BigNumber(heading='Presion media', value=media_presion, )
unidades_altitud = dp.BigNumber(heading='Altitud media', value=media_altitud, )
nombre = dp.BigNumber(heading='Equipo', value=nombres_equipo[0], )

#fichero=dp.Attachment(file='/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (Proyecto Completo)/2024.02.24_1-1.csv', filename='Proyecto Marte.csv')
fichero = dp.Attachment(file='C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/10 Elaboracion de Informes (Proyecto Completo)/2024.02.24_1-1.csv', filename='Proyecto Marte.csv')
texto = dp.Text('**Puedes descargar el fichero con los datos del informe:**')
#report = dp.Report(titulo, unidades_temperatura, unidades_presion, unidades_altitud, nombre,texto, fichero)

report = dp.Report(
    dp.Page(
        title='Informe',
        blocks=[titulo,dp.Media(ruta_imagen), unidades_temperatura, unidades_presion, unidades_altitud, nombre, texto, fichero]
    ),
    dp.Page(
        title='Grafico de lineas',
        blocks=[titulo2,dp.Media(ruta_imagen), grafico_datapane_lineas, texto, fichero]
    ),
    dp.Page(
        title='Datos',
        blocks=[titulo3,dp.Media(ruta_imagen), data_table, texto, fichero]
    )
)




#report.save(path="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (Proyecto Completo)/Proyecto Marte.html", open=True)
report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/10 Elaboracion de Informes (Proyecto Completo)/Proyecto Marte.html", open=True)
