#! /bin/bash

PATH_SCRIPT=..
PATH_M5OUT=./m5out
PATH_TEMPLATE=..
PATH_MCPATH=/home/jhon/mytools/mcpat
PATH_CONFIG=.

python2.7 $PATH_SCRIPT/gem5toMcPAT_cortexA76.py  $PATH_M5OUT/stats.txt $PATH_M5OUT/config.json $PATH_TEMPLATE/ARM_A76_2.1GHz.xml

$PATH_MCPATH/mcpat -infile $PATH_CONFIG/config.xml -print_level 5 -opt_for_Clk 1 > power_info.txt