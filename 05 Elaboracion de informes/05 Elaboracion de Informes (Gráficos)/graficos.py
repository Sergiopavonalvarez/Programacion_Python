
import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

fichero_csv = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/05 Elaboracion de Informes (Gráficos)/DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv)

#Grafico Lineas
ventas_mes = df.groupby(['Mes'], sort=False).sum()
grafico_matplot_lineas = ventas_mes.plot(y='Unidades')
grafico_datapane_lineas = dp.Plot(grafico_matplot_lineas, responsive=False)


#Grafico barras
ventas_vendedor = df.groupby(['Nombre']).sum()
grafico_matplot_barras = ventas_vendedor.plot.bar(y='Importe (€)')
plt.tight_layout()
grafico_datapane_barras = dp.Plot(grafico_matplot_barras, responsive=False)

#Grafico tarta
grafico_matplotlib_sectores = ventas_vendedor.plot.pie(y='Unidades', legend=False, ylabel="")
grafico_datapane_sectores = dp.Plot(grafico_matplotlib_sectores, responsive=False)



# Creamos un informe con los graficos:
#report = dp.Report(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores)


#Agrupados en dos columnas:
#report=dp.Report(
#    dp.Group(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores, columns=2)
#)


#Agrupados por paginas:
report = dp.Report(
    dp.Page(
        title='Grafico de lineas',
        blocks=[grafico_datapane_lineas]
    ),
    dp.Page(
        title='Grafico de Barras',
        blocks=[grafico_datapane_barras]
        ),
    dp.Page(
        title='Grafico de Sectores',
        blocks=[grafico_datapane_sectores]
)
)


#report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/05 Elaboracion de Informes (Gráficos)/Informe_barras(Sinagrupar en columnas).html", open=True)
report.save(path="/05 Elaboracion de informes/05 Elaboracion de Informes (Gráficos)/Informe_barras(Agrupados en columnas).html", open=True)

