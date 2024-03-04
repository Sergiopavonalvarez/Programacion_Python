import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

fichero_csv = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/DI_U05_A02_PP_E_01.csv")
df = pd.read_csv(fichero_csv)

image_path = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/DI_U05_A02_PP_E_02.png")  # Ruta de la imagen


title = dp.HTML('<p style="font-size: 50px; text-align: center; color: black;">Informe de Ventas</p>')
image = dp.Media(image_path)

ventas_2021 = df[df['Año'] == 2021]
ventas_totales_2021 = ventas_2021['Ventas'].sum()
Ventas_2020 = df[df['Año'] == 2020]
Ventas_Totales_2020 = Ventas_2020['Ventas'].sum()
VentasTotales = dp.BigNumber(heading='Ventas Totales 2021', value=ventas_totales_2021,
                             change=ventas_totales_2021 - Ventas_Totales_2020,
                             is_upward_change=Ventas_Totales_2020 < ventas_totales_2021)

titulo = dp.HTML('<p style="font-size: 50px; color: black;">Informe de Ventas</p>')
fichero = dp.Attachment(file='C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)//DI_U05_A02_PP_E_01.csv',
                        filename='Fichero CSV')

table = dp.Table(df)
data_table = dp.DataTable(df)

ventas_ano = df.groupby(['Año'], sort=False).sum()
grafico_matplot_lineas = ventas_ano.plot(y='Ventas')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

ventas_vendedor = df.groupby(['Región']).sum()
grafico_matplot_barras = ventas_vendedor.plot.bar(y='Ventas')
grafico_datapane_barras = dp.Plot(grafico_matplot_barras, responsive=False)

ventas_por_region = df.groupby('Tipo de producto')['Ventas'].sum()
plt.figure(figsize=(8, 8))
plt.pie(ventas_por_region, labels=ventas_por_region.index, autopct='%1.1f%%')
plt.title('Ventas por Región')
grafico_matplot_sectores = plt.gcf()
grafico_datapane_sectores = dp.Plot(grafico_matplot_sectores, responsive=False)

Ventastotalesgroup = dp.Group(VentasTotales, VentasTotales, columns=2)

# reportb= dp.Report(image, title, VentasTotales, data_table, fichero)
report = dp.Report(
    dp.Page(
        title='Inicio',
        blocks=[image, title, Ventastotalesgroup],
    ),
    dp.Page(
        title='Tablas',
        blocks=[data_table, fichero]
    ),
    dp.Page(
         title='Grafico de Ventas',
         blocks=[
             dp.Group(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores, columns=2),
         ]
    )
)


report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/11 Elaboracion de Informes (Completo 02)/prueba2.html", open=True)
