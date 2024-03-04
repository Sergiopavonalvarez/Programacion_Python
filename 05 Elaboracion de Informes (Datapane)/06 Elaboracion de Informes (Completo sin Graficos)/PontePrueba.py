import os
import pandas as pd
import datapane as dp

fichero_csv="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/06 Elaboracion de Informes (Completo sin Graficos)/DI_U05_A02_PP_E_01.csv"
ruta_imagen_local="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/06 Elaboracion de Informes (Completo sin Graficos)/DI_U05_A02_PP_E_02.png"
titulo = dp.HTML("<h1 style='text-align:center; color:#4CAF50;'>Informe: Análisis de Ventas 2021</h1>")

df=pd.read_csv(fichero_csv)
dp.Media(ruta_imagen_local)

año_2021=df[df['Año']==2021]
ventas_2021=año_2021['Ventas'].sum()
año_2020=df[df['Año']==2020]
ventas_2020=año_2020['Ventas'].sum()

data_table_config = dp.DataTable(df)


unidades_fin_año=dp.BigNumber(heading='Ventas totales en 2021',
                              value=ventas_2021,
                              change=ventas_2021 - ventas_2020,
                              is_upward_change=ventas_2020 < ventas_2021
                              )

fichero=dp.Attachment(file='C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/06 Elaboracion de Informes (Completo sin Graficos)/DI_U05_A02_PP_E_01.csv', filename='Ficher.csv')
texto=dp.Text('**Puedes descargar el fichero con los datos del informe.**')
report=dp.Report( titulo,dp.Media(ruta_imagen_local),unidades_fin_año, data_table_config, fichero)
report.save(path='C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/06 Elaboracion de Informes (Completo sin Graficos)/Ponte a Prueba.html', open=True)