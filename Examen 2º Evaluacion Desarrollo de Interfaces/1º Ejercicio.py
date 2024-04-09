import datapane as dp
import pandas as pd
import matplotlib.pyplot as plt

fichero_csv = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/Examen 2º Evaluacion Desarrollo de Interfaces/DatosOrigen.csv")
df = pd.read_csv(fichero_csv)

image_path = ("C:/Users/pavon/Documents/PyCharm/Programacion_Python/Examen 2º Evaluacion Desarrollo de Interfaces/Logo.png")  # Ruta de la imagen

titulo = dp.HTML('<p style="font-size: 70px; text-align: Left; color: blue;">Examen</p>')
imagen = dp.Media(image_path)

ventas2024 = df[df['AnyoFacturacion'] == 2024]
ventas_totales_2024 = ventas2024['Importe'].sum()

ventas2017 = df[df['AnyoFacturacion'] == 2017]
ventas_totales_2017 = ventas2017['Importe'].sum()

ventas_2021_big_number = dp.BigNumber(
    heading='Importe total de ventas en 2024',
    value=ventas_totales_2024,
    change=ventas_totales_2024 - ventas_totales_2017,
    is_upward_change=ventas_totales_2024 > ventas_totales_2017
)

ventas_Madrid_2024 = df[(df['Tienda'] == 'Madrid') & (df['AnyoFacturacion'] == 2024)]
ventas_totales_Madrid = ventas_Madrid_2024['Importe'].sum()
ventas_Madrid_big_number = dp.BigNumber(
    heading='Total Ventas Madrid 2024',
    value=ventas_totales_Madrid
)

ventas_Sevilla_2024 = df[(df['Tienda'] == 'Sevilla') & (df['AnyoFacturacion'] == 2024)]
ventas_totales_Sevilla = ventas_Sevilla_2024['Importe'].sum()
ventas_Sevilla_big_number = dp.BigNumber(
    heading='Total Ventas Sevilla 2024',
    value=ventas_totales_Sevilla
)

ventas_Barcelona_2024 = df[(df['Tienda'] == 'Barcelona') & (df['AnyoFacturacion'] == 2024)]
ventas_totales_Barcelona = ventas_Barcelona_2024['Importe'].sum()
ventas_Barcelona_big_number = dp.BigNumber(
    heading='Total Ventas Barcelona 2024',
    value=ventas_totales_Barcelona
)

ventas_Valencia_2024 = df[(df['Tienda'] == 'Valencia') & (df['AnyoFacturacion'] == 2024)]
ventas_totales_Valencia = ventas_Valencia_2024['Importe'].sum()
ventas_Valencia_big_number = dp.BigNumber(
    heading='Total Ventas Valencia 2024',
    value=ventas_totales_Valencia
)

table = dp.Table(df)
data_table = dp.DataTable(df)


descargarfichero = dp.Attachment(file='/Examen 2º Evaluacion Desarrollo de Interfaces/DatosOrigen.csv', filename='Datos ventas.csv')
texto = dp.Text('**Puedes descargar el fichero con los datos del informe:**')

report2=dp.Report(
    dp.Group(ventas_Madrid_big_number,ventas_Sevilla_big_number,ventas_Barcelona_big_number,ventas_Valencia_big_number, columns=2)
)

report = dp.Report( imagen,titulo,ventas_2021_big_number,report2, data_table,texto,descargarfichero)
report.save(path="/Examen 2º Evaluacion Desarrollo de Interfaces/Ejercicio01.html", open=True)
