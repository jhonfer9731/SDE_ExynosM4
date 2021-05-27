import os
import sys
import datetime as dt
import json
import time
import pandas as pd
carpeta= '/home/jhon/mytools/workloads/jpeg2k_dec/results_sim_predictor6/'
params=['final_tick','system.cpu.cpi_total','host_seconds']

tabla_simu = pd.DataFrame(columns=params)

indexFile=0
for base, dirs, files in os.walk(carpeta):
    
    for nombreArchivo in files:

        if "stats" not in nombreArchivo: continue

        values=[]
        nombreArchivo_2=base+nombreArchivo

        """ Se abre el archivo de estadisticas para el procesador Exynos M4 """

        try:
            stats_file = open(nombreArchivo_2)
        except IOError:
            print("******ERROR: File not found or can't open stat file******")
            sys.exit(1)

        stats_file = stats_file.read().split(r"%%")[1]
        stats = json.loads(stats_file)
        stats_red = {}

        stats_red["nombre_archivo"] = nombreArchivo
        for parametro in params:

            stats_red[parametro] = stats[parametro]

        tabla_simu = tabla_simu.append(stats_red,ignore_index=True) # Se agrega una simulacion a la tabla



print(tabla_simu)


    


        