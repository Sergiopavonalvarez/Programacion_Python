

import datapane as dp
import pandas as pd

fichero_csv="C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/Datapane/DI_U05_A02_02.csv"
df=pd.read_csv(fichero_csv)
table=dp.Table(df)
data_table=dp.DataTable(df)
report_imprimir=dp.Report(table)
report_imprimir.save(path="C:/Users/pavon/Documents/PyCharm/Programacion_Python/04 Componentes de Usuario/Datapane/DI_U05_A01_01.html", open=True)


