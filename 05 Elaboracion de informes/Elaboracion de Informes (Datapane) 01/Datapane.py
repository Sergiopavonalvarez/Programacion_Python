

import datapane as dp
import pandas as pd

fichero_csv="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes/Elaboracion de Informes (Datapane) 01/DI_U05_A02_02.csv"
df=pd.read_csv(fichero_csv)
table=dp.Table(df)
data_table=dp.DataTable(df)
report_imprimir=dp.Report(table)
report_imprimir.save(path='Informe_01.html', open=True)


