from analizadorest5.sintacticot5 import parser
from analizadorest5.sintacticot5 import names

ruta="Tareas.csv"
archivo= open(ruta,'r')
next(archivo, None)
datos=archivo.read()
archivo.close()
parser.parse(datos)


"""for filas in archivo:
    filas.rstrip()
    temporal=filas.split(",")
    cadena= str(temporal)
    listaT.append(temporal)"""

""""print(datos)
print("\n-Datos obtenidos.-\n")"""



