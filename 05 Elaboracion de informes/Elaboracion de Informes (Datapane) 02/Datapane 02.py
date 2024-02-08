import os
import pandas as pd
import datapane as dp

fichero_csv="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/Elaboracion de Informes (Datapane) 02/"
os.chdir(fichero_csv)
fichero_csvv="DI_U05_A02_02.csv"
df=pd.read_csv(fichero_csvv) #Cargamos el archivo CSV en un DataFrame

datos_diciembre=df[df['Mes']=='Diciembre'] #Filtramos los datos del mes diciembre
unidades_diciembre=datos_diciembre['Unidades'].sum()#Sumar las unidades vendidas en el mes de diciembre.

datos_noviembre=df[df['Mes']=='Noviembre']#Filtramos los datos del mes noviembre
unidades_noviembre=datos_noviembre['Unidades'].sum()#Sumar las unidades vendidas en el mes de noviembre

unidades_fin_año=dp.BigNumber(heading='Unidades totales en diciembre',
                              value=unidades_diciembre,
                              change=unidades_diciembre-unidades_noviembre,
                              is_upward_change=unidades_diciembre>unidades_noviembre)

datos_febrero=df[df['Mes']=='Febrero']
unidades_febrero=datos_febrero['Unidades'].sum()

datos_enero=df[df['Mes']=='Enero']
unidades_enero=datos_enero['Unidades'].sum()

unidades_fin_año2=dp.BigNumber(heading='Unidades totales en Febrero',
                              value=unidades_febrero,
                              change=unidades_febrero-unidades_enero,
                              is_upward_change=unidades_enero>unidades_febrero)


report=dp.Report(unidades_fin_año, unidades_fin_año2)#Mostrar el resultado en el navegador

report.save(path='Informe 02.html', open=True)#Guardar resultado en ese archivo

