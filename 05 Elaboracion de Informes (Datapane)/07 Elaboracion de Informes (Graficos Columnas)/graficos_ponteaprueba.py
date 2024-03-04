import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt
import sns

# Ruta al archivo CSV
#fichero_csv = "/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/07 Elaboracion de Informes (Graficos Columnas)/DI_U05_A02_PP_E_01.csv"
fichero_csv = "C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/07 Elaboracion de Informes (Graficos Columnas)/DI_U05_A02_PP_E_01.csv"


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


####################################################################
# Filtrar solo las filas correspondientes a la región 'Norte'
df_norte = df[df['Región'] == 'Norte'].groupby(['Año']==2021).sum()

# Calcular las ventas por vendedor para la región 'Norte'
ventas_vendedor_norte = df_norte.groupby(['Vendedor']).sum()

# Crear el gráfico de barras
grafico_matplot_barras_norte = ventas_vendedor_norte.plot.bar(y='Ventas')
plt.tight_layout()

# Crear el gráfico de Datapane
grafico_datapane_barras_norte = dp.Plot(grafico_matplot_barras_norte, responsive=False)

#####################################################################







#Grafico tarta
ventas_vendedors = df.groupby(['Tipo de producto']).sum()
grafico_matplotlib_sectores = ventas_vendedors.plot.pie(y='Ventas', legend=False, ylabel="")
grafico_datapane_sectores = dp.Plot(grafico_matplotlib_sectores, responsive=False)



# Creamos un informe con los graficos:
#report = dp.Report(grafico_datapane_lineas,grafico_datapane_barras,grafico_datapane_sectores)


#Agrupados en dos columnas:
report=dp.Report(
    dp.Group(grafico_datapane_lineas, grafico_datapane_barras, grafico_datapane_sectores,grafico_datapane_barras_norte, columns=2)
)

report.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/07 Elaboracion de Informes (Graficos Columnas)/Informe_barras(Sin agrupar en columnas).html", open=True)
#report.save(path="/Users/sergiopavonalvarez/Programacion/PycharmProjects/Programacion_Python/05 Elaboracion de informes/07 Elaboracion de Informes (Graficos Columnas)/Informe(Ponte a Prueba).html", open=True)

