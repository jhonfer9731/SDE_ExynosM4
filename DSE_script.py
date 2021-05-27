import os
import sys
import datetime as dt
import json
import time
import pandas as pd
carpeta= 'm5out/'
params=['final_tick','system.cpu.cpi_total','host_seconds']

tabla_simu = pd.DataFrame(columns=params)

indexFile=0
for base, dirs, files in os.walk(carpeta):
    
    for nombreArchivo in files:

        if "stats" not in nombreArchivo: continue

        values=[]
        nombreArchivo=base+nombreArchivo

        """ Se abre el archivo de estadisticas para el procesador Exynos M4 """

        try:
            stats_file = open(nombreArchivo)
        except IOError:
            print("******ERROR: File not found or can't open stat file******")
            sys.exit(1)

        stats = {}
        count = 2
        for line in stats_file:
            
            if "---" in line: continue
            lineArray = line.split(" ")
            name = lineArray[0]   #we got name from stat file
            if name not in params: continue # Se descarta los parametros que no se quieran seleccionar y por lo tanto no estan en la lista params
            val = ''
            for e in lineArray:
                try:
                    val = int(e)            #int value from each line
                except ValueError:
                    try:
                        val = float(e)      #float value from each line
                    except ValueError:
                        continue

            #print "%d Name: %s \tValue: %s" %(count,Name ,val)
            count += 1
            stats[name] = val               #storing the value in stat array
        tabla_simu = tabla_simu.append(stats,ignore_index=True) # Se agrega una simulacion a la tabla



print(tabla_simu)


    


        