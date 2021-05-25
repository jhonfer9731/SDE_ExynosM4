import os
import sys

GEM5PATH="/home/jhon/mytools/gem5/build/ARM"
SCRIPTPATH="/home/jhon/mytools/gem5/configs/tutorial/ExynosM4"
WORKLOADS="/home/jhon/mytools/workloads"


memCacheL1ISize = ['32KB','128KB','256KB']

for size in memCacheL1ISize:

    MOREOPTIONS="--l1i_size="+size
    comando = f'{GEM5PATH}/gem5.fast {SCRIPTPATH}/ExynosM4.py --cmd={WORKLOADS}/jpeg2k_dec/jpg2k_dec --options="-i jpg2kdec_testfile.j2k -o jpg2kdec_outfile.bmp" {MOREOPTIONS}'
    os.system(comando)

    """ Se abre el archivo de estadisticas para el procesador Exynos M4 """

    try:
        stats_file = open("m5out/stats.txt")
    except IOError:
        print("******ERROR: File not found or can't open stat file******")
        sys.exit(1)

    stats = {}
    count = 2
    for line in stats_file:
        if "---" in line: continue
        lineArray = line.split(" ")
        Name = lineArray[0]             #we got name from stat file
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
        stats[Name] = val               #storing the value in stat array
    print(stats)

    