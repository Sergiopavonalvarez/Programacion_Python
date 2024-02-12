import os
import pandas as pd
import datapane as dp

fichero_csv="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/Elaboracion de Informes (Ponte a Prueba) 06/"
os.chdir(fichero_csv)
fichero_csvv="DI_U05_A02_PP_E_01.csv"
df=pd.read_csv(fichero_csvv) #Cargamos el archivo CSV en un DataFrame

datos_diciembre=df[df['Mes']=='Diciembre'] #Filtramos los datos del mes diciembre
unidades_diciembre=datos_diciembre['Unidades'].sum()#Sumar las unidades vendidas en el mes de diciembre.

datos_noviembre=df[df['Mes']=='Noviembre']#Filtramos los datos del mes noviembre
unidades_noviembre=datos_noviembre['Unidades'].sum()#Sumar las unidades vendidas en el mes de noviembre

unidades_fin_año=dp.BigNumber(heading='Unidades totales en diciembre',
                              value=unidades_diciembre,
                              change=unidades_diciembre-unidades_noviembre,
                              is_upward_change=unidades_diciembre>unidades_noviembre)

report=dp.Report(unidades_fin_año)#Mostrar el resultado en el navegador

report.save(path='Ponte a Prueba.html', open=True)#Guardar resultado en ese archivo