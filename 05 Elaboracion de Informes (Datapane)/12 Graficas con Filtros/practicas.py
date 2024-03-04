import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

fichero_csv = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/DI_U05_A02_PP_E_01.csv")
df = pd.read_csv(fichero_csv)

ventas_vendedor = df.groupby(['Año']).sum()
grafico_matplot_barras = ventas_vendedor.plot.bar(y='Ventas')
grafico_datapane_barras = dp.Plot(grafico_matplot_barras, responsive=False)

# Un gráfico de lineas, con las ventas para cada una de las regiones en el año 2021
ventas_region_2021 = df[df['Año'] == 2021].groupby(['Región']).sum()
grafico_matplot_lineas = ventas_region_2021.plot(y='Ventas')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

# Un gráfico de barras, con las ventas para cada una de las regiones en el año 2017
ventas_region_2017 = df[df['Año'] == 2017].groupby(['Región']).sum()
grafico_matplot_barras_2017 = ventas_region_2017.plot.bar(y='Ventas')
grafico_datapane_barras_2017 = dp.Plot(grafico_matplot_barras_2017, responsive=False)

# Un gráfico de barras que represente el reparto de las ventas totales entre los distintos tipos de producto
ventas_por_tipo = df.groupby('Tipo de producto')['Ventas'].sum()
grafico_matplot_barras_tipo = ventas_por_tipo.plot.bar()
grafico_datapane_barras_tipo = dp.Plot(grafico_matplot_barras_tipo, responsive=False)


report = dp.Report(grafico_datapane_barras, grafico_datapane_lineas, grafico_datapane_barras_2017, grafico_datapane_barras_tipo)

report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/informe.html", open=True)
