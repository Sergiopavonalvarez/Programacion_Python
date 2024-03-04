import datapane as dp
import pandas as pd

fichero_csv ="C:/Users/pavon/Documents/PyCharm/Programacion_Python/05 Elaboracion de informes (Datapane)/04 Elaboracion de Informes (SQL)/DI_U05_A02_02.csv" # Ruta del fichero origen de los datos.
df = pd.read_csv(fichero_csv) # Cargamos el fichero en un DataFrame.

table = dp.Table(df) # Creamos un objeto tabla con los datos del DataFrame. 
data_table = dp.DataTable(df) # Creamos un objeto DataTable con los datos del DataFrame.

# INFORME IMPRIMIR
report_imprimir = dp.Report(table) # Creamos un informe con la tabla.
report_imprimir.save(path="/05 Elaboracion de Informes (Datapane)/04 Elaboracion de Informes (SQL)/Imprimir.html", open=True) # Guardamos el informe en un fichero HTML y lo abrimos al lanzar la aplicación.

# INFORME VISUALIZAR
report_visualizar = dp.Report(data_table) # Creamos un informe con la DataTable.
report_visualizar.save(path="/05 Elaboracion de Informes (Datapane)/04 Elaboracion de Informes (SQL)/Visualizar.html", open=True) # Guardamos el informe en un fichero HTML y lo abrimos al lanzar la aplicación.

# INFORME COMPLETO
report = dp.Report(data_table,table) # Creamos un informe con la tabla y la DataTable.
report.save(path="/05 Elaboracion de Informes (Datapane)/04 Elaboracion de Informes (SQL)/Completo.html", open=True) # Guardamos el informe en un fichero HTML y lo abrimos al lanzar la aplicación.


#Querys:
# SELECT * FROM $table WHERE Unidades <300 AND Mes='Agosto'
#
#