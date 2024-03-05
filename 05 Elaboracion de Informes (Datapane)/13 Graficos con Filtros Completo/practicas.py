import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

fichero_csv = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/DI_U05_A02_PP_E_01.csv")
df = pd.read_csv(fichero_csv)

image_path = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/DI_U05_A02_PP_E_02.png")  # Ruta de la imagen


title = dp.HTML('<p style="font-size: 50px; text-align: center; color: black;">Examen</p>')
image = dp.Media(image_path)

ventas2021 = df[df['Año'] == 2021]
ventas_totales_2021 = ventas2021['Ventas'].sum()

ventas2017 = df[df['Año'] == 2017]
ventas_totales_2017 = ventas2017['Ventas'].sum()
ventas_2021_big_number = dp.BigNumber(
    heading='Ventas Totales 2021',
    value=ventas_totales_2021,
    change=ventas_totales_2021 - ventas_totales_2017,
    is_upward_change=ventas_totales_2021 > ventas_totales_2017
)

# Filtrar las ventas de la región 'Norte' en el año 2021
ventas_norte_2021 = df[(df['Región'] == 'Norte') & (df['Año'] == 2021)]
# Sumar las ventas de la región 'Norte' en el año 2021
ventas_totales_norte_2021 = ventas_norte_2021['Ventas'].sum()
# Crear un objeto BigNumber con las ventas totales de la región 'Norte' en el año 2021
ventas_norte_2021_big_number = dp.BigNumber(
    heading='Ventas Totales Norte 2021',
    value=ventas_totales_norte_2021
)

ventar_sur_2020 = df[(df['Región'] == 'Sur') & (df['Año'] == 2020)]
ventas_totales_sur_2020 = ventar_sur_2020['Ventas'].sum()
ventas_sur_2020_big_number = dp.BigNumber(
    heading='Ventas Totales Sur 2020',
    value=ventas_totales_sur_2020
)


#################Graficos####################
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

gruposGraficos = dp.Group(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_barras_2017,
                          grafico_datapane_barras_tipo, columns=2)

#################Descaragar Fichero####################
fichero = dp.Attachment(file='C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/DI_U05_A02_PP_E_01.csv',
                        filename='Fichero CSV')

report = dp.Report(title, image, ventas_2021_big_number, ventas_norte_2021_big_number, ventas_sur_2020_big_number,
                   gruposGraficos, fichero)

report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/informe.html", open=True)
