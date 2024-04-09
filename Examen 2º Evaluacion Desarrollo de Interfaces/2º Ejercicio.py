import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

fichero_csv = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/Examen 2º Evaluacion Desarrollo de Interfaces/DatosOrigen.csv")
df = pd.read_csv(fichero_csv)



ventas = df.groupby(['AnyoFacturacion']).sum()
grafico_matplot_barras = ventas.plot.bar(y='Importe')
plt.tight_layout()
grafico_datapane_barras = dp.Plot(grafico_matplot_barras, responsive=False)


ventas_2024 = df[df['AnyoFacturacion'] == 2024].groupby(['Tienda']).sum()
plot_lineas = ventas_2024.plot(y='Importe')
lineas_2024 = dp.Plot(plot_lineas, responsive=False)




ventas_2017 = df[df['AnyoFacturacion'] == 2017].groupby(['Tienda']).sum()
plot_barras_2017 = ventas_2017.plot.bar(y='Importe')
barras_2017 = dp.Plot(plot_barras_2017, responsive=False)




ventas_por_tipo = df.groupby('Producto')['Importe'].sum()
portipo = ventas_por_tipo.plot.bar()
barras_tipo = dp.Plot(portipo, responsive=False)



report=dp.Report(
    dp.Group(grafico_datapane_barras, lineas_2024, barras_2017,barras_tipo, columns=2)
)



report.save(path="/Examen 2º Evaluacion Desarrollo de Interfaces/Ejercicio02.html", open=True)
