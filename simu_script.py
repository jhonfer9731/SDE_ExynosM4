import os
import sys
import datetime as dt
import json
import time
import random


GEM5PATH="/home/jhon/mytools/gem5/build/ARM"
SCRIPTPATH="/home/jhon/mytools/gem5/configs/tutorial/ExynosM4"
#WORKLOADS="/home/jhon/mytools/workloads/HelloWord/hello_arm64"
WORKLOADS="/home/jhon/mytools/workloads/jpeg2k_dec/jpg2k_dec"
""" Parametros a variar para las cache """

parametros = {"memCacheL1ISize" : ['8kB','16kB','32kB','64kB','128kB','256kB','512kB'], # --l1i_size
"memCacheL1DSize" : ['8kB','16kB','32kB','64kB','128kB','256kB','512kB'], # --l1d_size
"memCacheL2Size" : ['16kB','32kB','64kB','128kB','256kB','512kB'],  # --l2_size
"memCacheL1I_Assoc" : [4,8,16,32,64], #--l1i_assoc
"memCacheL1D_Assoc" : [4,8,16,32,64], #--l1d_assoc
"memCacheL2_Assoc" : [4,8,16,32,64], #--l2_assoc
"decRenameComWidth" : [8,10,12], # --decode_width ,--rename_width, --commit_width, --wb_width
"dispatchIssueWidth" : [8,10,12],# --dispatch_width, --issue_width
#"fetchEntries" : [64,128,256],#  --fb_entries, --fq_entries, --iq_entries
"robEntries" : [100,300,500],# --rob_entries
"loadStoreQueue" : [16,64,128],# --lq_entries, --sq_entries
#"branchCompare" : [2,3],# --num_fu_cmp
"intALU" : [3,4,5]# --num_fu_intALU
#"divMult" : [1,3],# --num_fu_intDIVMUL
#"fuRead" : [2,3],# --num_fu_read
#"fuWrite" : [2,3]

}#  --num_fu_write


for i in range(10):

    parametros_rand = {} 
    for key,value in parametros.items():
        parametros_rand[key] = random.choice(value) # Diccionario con los valores que seran escogidos de forma aleatoria para cada simulación
    print("\n\n\n")
    print("Se ejecuta Simulación #",i)
    print("\n\n\n")
    print(parametros_rand)         

    MOREOPTIONS=f'"--l1i_size={parametros_rand["memCacheL1ISize"]}" "--l1d_size={parametros_rand["memCacheL1DSize"]}" "--l2_size={parametros_rand["memCacheL2Size"]}" "--l1i_assoc={parametros_rand["memCacheL1I_Assoc"]}" "--l1d_assoc={parametros_rand["memCacheL1D_Assoc"]}" "--l2_assoc={parametros_rand["memCacheL2_Assoc"]}" "--decode_width={parametros_rand["decRenameComWidth"]}" "--rename_width={parametros_rand["decRenameComWidth"]}" "--commit_width={parametros_rand["decRenameComWidth"]}" "--wb_width={parametros_rand["decRenameComWidth"]}" "--dispatch_width={parametros_rand["dispatchIssueWidth"]}" "--issue_width={parametros_rand["dispatchIssueWidth"]}" "--rob_entries={parametros_rand["robEntries"]}" "--lq_entries={parametros_rand["loadStoreQueue"]}" "--sq_entries={parametros_rand["loadStoreQueue"]}" "--num_fu_intALU={parametros_rand["intALU"]}"'

    comando = f'time {GEM5PATH}/gem5.fast {SCRIPTPATH}/ExynosM4.py --cmd={WORKLOADS} --options="-i jpg2kdec_testfile.j2k -o jpg2kdec_outfile.bmp" {MOREOPTIONS}'
    os.system(comando)

    time.sleep(5) # Espera un tiempo por si algun archivo aun no este listo en la carpeta

    fecha_simu = dt.datetime.today().isoformat(timespec='seconds')
    try:
        os.rename("m5out/config.json",f"results_sim/config_{fecha_simu}.json")
        os.rename("m5out/stats.txt",f"results_sim/stats_{fecha_simu}.txt")
    except Exception as e:
        print(e)

    fileParams = open(f"results_sim/params_simu_{fecha_simu}.txt","w")
    fileParams.write(f'Parametros Modificados:\n\n{MOREOPTIONS}\n\n%%')
    fileParams.close()

        