import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

# Ruta al archivo CSV
#fichero_csv = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/Elaboracion de Informes (Ponte a Prueba) 07/DI_U05_A02_PP_E_01.csv"
fichero_csv ="C:/Users/pavon/Documents/VS Code/Python/Programacion_Python/05 Elaboracion de informes/Elaboracion de Informes (Ponte a Prueba) 07/DI_U05_A02_PP_E_01.csv"
# Cargar el DataFrame desde el archivo CSV
df = pd.read_csv(fichero_csv)

# Gráfico de líneas
ventas_mes = df.groupby(['Año'], sort=False).sum()
grafico_matplot_lineas = ventas_mes.plot(y='Ventas')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)

# Gráfico de barras
ventas_vendedor = df.groupby(['Región']).sum()
grafico_matplot_barras = ventas_vendedor.plot.bar(y='Ventas')
plt.tight_layout()
grafico_datapane_barras = dp.Plot(grafico_matplot_barras, responsive=False)

# Gráfico de tarta
ventas_vendedors = df.groupby(['Tipo de producto']).sum()
grafico_matplotlib_sectores = ventas_vendedors.plot.pie(y='Ventas', legend=False, ylabel="")
grafico_datapane_sectores = dp.Plot(grafico_matplotlib_sectores, responsive=False)

# Crear un informe con los gráficos
report = dp.Report(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores)

# Guardar el informe como archivo HTML
report.save(path="Informe_Graficos.html", open=True)
