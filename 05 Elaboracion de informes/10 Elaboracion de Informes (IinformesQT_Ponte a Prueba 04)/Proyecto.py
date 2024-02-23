import os
import pandas as pd
import datapane as dp

#fichero_csv="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/02 Elaboracion de Informes (Datapane)/"
fichero_csv="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)"
os.chdir(fichero_csv)
fichero_csvv="2024.02.24_1-1.csv"
df=pd.read_csv(fichero_csvv)
print(df.columns)
titulo = dp.HTML("<h1 style='text-align:center; color:#4CAF50;'>Informe: Marte 2021</h1>")


datos_diciembre = df[df[' Temperatura_[ºC]'] == 'Paquete']
unidades_temperatura = datos_diciembre['Paquete'].sum()

datos_diciembre_presion = df[df['Presion_[Pa]'] == 'Paquete']
unidades_presion = datos_diciembre_presion['Paquete'].sum()

datos_diciembre_altitud = df[df['Altitud_[m]'] == 'Paquete']
unidades_altitud = datos_diciembre_altitud['Paquete'].sum()

unidades_fin_año_temperatura = dp.BigNumber(heading='Unidades de Temperatura',
                                            value=unidades_temperatura,
)

unidades_fin_año_presion = dp.BigNumber(heading='Unidades de Presion',
                                        value=unidades_presion,
)

unidades_fin_año_altitud = dp.BigNumber(heading='Unidades de Altitud',
                                        value=unidades_altitud,
)



fichero=dp.Attachment(file='/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04/2024.02.24_1-1.csv', filename='Proyecto Marte.csv')
texto=dp.Text('**Puedes descargar el fichero con los datos del informe.**')
report = dp.Report(titulo,unidades_fin_año_temperatura, unidades_fin_año_presion, unidades_fin_año_altitud,texto)

report.save(path="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/10 Elaboracion de Informes (IinformesQT_Ponte a Prueba 04)/Proyecto Marte.html", open=True)#Guardar resultado en ese archivo