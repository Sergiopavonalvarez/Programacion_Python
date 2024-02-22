import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
fichero_csv = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/07 Elaboracion de Informes (Ponte a Prueba)/DI_U05_A02_PP_E_01.csv"

# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv(fichero_csv)

#Grafico Lineas
ventas_mes = df.groupby(['Año'], sort=False).sum()
grafico_matplot_lineas = ventas_mes.plot(y='Ventas')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)


#Grafico barras
ventas_vendedor = df.groupby(['Región']).sum()
grafico_matplot_barras = ventas_vendedor.plot.bar(y='Ventas')
plt.tight_layout()
grafico_datapane_barras = dp.Plot(grafico_matplot_barras, responsive=False)

#Grafico tarta
ventas_vendedors = df.groupby(['Tipo de producto']).sum()
grafico_matplotlib_sectores = ventas_vendedors.plot.pie(y='Ventas', legend=False, ylabel="")
grafico_datapane_sectores = dp.Plot(grafico_matplotlib_sectores, responsive=False)



# Creamos un informe con los graficos:
#report = dp.Report(grafico_datapane_lineas,grafico_datapane_barras,grafico_datapane_sectores)


#Agrupados en dos columnas:
report=dp.Report(
    dp.Group(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores, columns=2)
)

#report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/05 Elaboracion de Informes (Gráficos)/Informe_barras(Sinagrupar en columnas).html", open=True)
report.save(path="/05 Elaboracion de informes/07 Elaboracion de Informes (Ponte a Prueba)/Informe(Ponte a Prueba).html", open=True)

