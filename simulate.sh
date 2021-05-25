#! /bin/bash

GEM5PATH=/home/jhon/mytools/gem5/build/ARM
SCRIPTPATH=/home/jhon/mytools/gem5/configs/tutorial/ExynosM4
WORKLOADS=/home/jhon/mytools/workloads

MOREOPTIONS=""

#! $GEM5PATH/gem5.fast $SCRIPTPATH/ExynosM4.py --cmd=/home/jhon/mytools/workloads/HelloWord/hello_arm64

$GEM5PATH/gem5.fast $SCRIPTPATH/ExynosM4.py --cmd=$WORKLOADS/jpeg2k_dec/jpg2k_dec --options="-i jpg2kdec_testfile.j2k -o jpg2kdec_outfile.bmp" $MOREOPTIONS