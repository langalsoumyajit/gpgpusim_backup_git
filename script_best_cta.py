import subprocess
import os
import re

#---------------------------------Change file name------------------------------------------------------------------------------------------------------------------
file_list = ["CONS_FFT_4_4.txt", "CONS_FFT_4_5.txt", "CONS_FFT_4_6.txt", "CONS_FFT_4_7.txt", "CONS_FFT_4_8.txt", "CONS_FFT_5_4.txt", "CONS_FFT_5_5.txt", "CONS_FFT_5_6.txt", "CONS_FFT_5_7.txt", "CONS_FFT_5_8.txt", "CONS_FFT_6_4.txt", "CONS_FFT_6_5.txt", "CONS_FFT_6_6.txt", "CONS_FFT_6_7.txt", "CONS_FFT_6_8.txt", "CONS_FFT_7_4.txt", "CONS_FFT_7_5.txt", "CONS_FFT_7_6.txt", "CONS_FFT_7_7.txt", "CONS_FFT_7_8.txt", "CONS_FFT_8_4.txt", "CONS_FFT_8_5.txt", "CONS_FFT_8_6.txt", "CONS_FFT_8_7.txt", "CONS_FFT_8_8.txt"]
#file_list = ["CONS_FFT_16__6_7.txt", "CONS_FFT_18__6_7.txt", "CONS_FFT_20__6_7.txt", "CONS_FFT_22__6_7.txt", "CONS_FFT_24__6_7.txt"]
#file_list = ["BLK_FFT_16__6_7.txt", "BLK_FFT_18__6_7.txt", "BLK_FFT_20__6_7.txt", "BLK_FFT_22__6_7.txt", "BLK_FFT_24__6_7.txt"]
str_gpu_ipc = "gpu_tot_ipc =     "

ipc_dict = {}

for file_i in file_list:
	ipc_list = []
	f1 = open(file_i, 'r')
	lines = str(f1.read())
	line_list = lines.split("\n")
	for line in line_list:
		if str_gpu_ipc in line:	
			ipc = re.findall("\d+\.\d+", line)
			#print(float(ipc[0]))
			ipc_list.append(float(ipc[0]))
	f1.close()
	#print(ipc_list)
	ipc_dict[file_i] = (ipc_list[-1]) 
#print(ipc_dict)

max_key = max(ipc_dict, key=ipc_dict.get)
print(max_key + " " + str(ipc_dict[max_key]))
print(file_list[-1] + " " + str(ipc_dict[file_list[-1]]))

