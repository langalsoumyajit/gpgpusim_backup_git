# Writing to an excel
# sheet using Python
import xlwt
import itertools
from xlwt import Workbook
import subprocess
import os
import re
import sys

app_list1 = ["3DS", "BFS2", "BLK", "BP", "CFD", "CONS", "FFT", "FWT", "GUPS", "HISTO", "HS", "JPEG", "LIB", "LPS", 
		"LUD", "LUH", "NN", "NW", "RAY", "RED", "SAD", "SC", "SCAN", "SCP", "SRAD", "TRD"]

all_combinations = []
wb = Workbook()
file_list = []
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet_1')
i = 0

str_gpu_ipc = "gpu_tot_ipc ="
str_gpu_dram_stall = "gpu_stall_dramfull ="
str_L2_MPKI_1 = "Avg_MPKI_Stream1="
str_L2_MPKI_2 = "Avg_MPKI_Stream2="

for r in range(2,3):
    combinations_object = itertools.combinations(app_list1, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list
for i in range(len(all_combinations)):
    #sheet1.write(i, 0, all_combinations[i][0])
    #sheet1.write(i, 1, all_combinations[i][1])
    #print(all_combinations[i][0] + "_" + all_combinations[i][1] + "_4_4.txt")
    file_name = all_combinations[i][0] + "_" + all_combinations[i][1] + "_4_4_3k.txt"
    file_list.append(file_name)
i = 1
sheet1.write(0, 0, "File_Name")
sheet1.write(0, 1, "IPC")
sheet1.write(0, 2, "MPKI_App1")
sheet1.write(0, 3, "MPKI_App2")
for file_i in file_list:
    f1 = open(file_i, 'r')
    lines = str(f1.read())
    line_list = lines.split("\n")
    ipc = 0
    dram_stall = 0
    mpki1 = 0
    mpki2 = 0
    for line in line_list:
        if str_gpu_ipc in line:	
            ipc = re.findall("\d+\.\d+", line)
            #print(ipc)
            #print(float(ipc[0]))
        if str_gpu_dram_stall in line:	
            dram_stall = re.findall("\d+", line)
            #print(dram_stall)
            #print(float(ipc[0]))
        if str_L2_MPKI_1 in line:	
            mpki1 = re.findall("\d+\.\d+", line)
            #print(mpki1)
            #print(float(ipc[0]))
        if str_L2_MPKI_2 in line:	
            mpki2 = re.findall("\d+\.\d+", line)
            #print(mpki2)
            #print(float(ipc[0]))
    sheet1.write(i, 0, file_i)
    sheet1.write(i, 1, ipc)
    sheet1.write(i, 2, mpki1)
    sheet1.write(i, 3, mpki2)
    i = i + 1
    f1.close()
    
wb.save('xlwt example.xls')
