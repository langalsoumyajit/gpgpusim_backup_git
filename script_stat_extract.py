import subprocess
import os
import re
import sys

#------------------------------- Invalid number of argument checker------------------------
if(len(sys.argv) == 5):
	print("Good to go")
elif(len(sys.argv) == 3):
	exit("ERROR !!!! : Please enter end CTA values")
else:
	exit("ERROR !!!! : Please enter two applications name with a space in between and initial CTAs")
#------------------------------------------------------------------------------------------

#-------------------------------It will create the file list-------------------------------
cta_num0_end = int(sys.argv[3]) + 1
cta_num1_end = int(sys.argv[4]) + 1
app1 = sys.argv[1]
app2 = sys.argv[2]
file_name = ""
file_list = []
print(app1 + " " + app2)
for i in range(4,cta_num0_end):
	for j in range(4,cta_num1_end):
		file_name = app1 + "_" + app2 + "_" + str(i) + "_" + str(j) + ".txt"
		file_list.append(file_name)
#---------------------------------Change file name------------------------------------------------------------------------------------------------------------------
"""file_list = ["CONS_FFT_4_4.txt", "CONS_FFT_4_5.txt", "CONS_FFT_4_6.txt", "CONS_FFT_4_7.txt", "CONS_FFT_4_8.txt", "CONS_FFT_5_4.txt", "CONS_FFT_5_5.txt", "CONS_FFT_5_6.txt", "CONS_FFT_5_7.txt", "CONS_FFT_5_8.txt", "CONS_FFT_6_4.txt", "CONS_FFT_6_5.txt", "CONS_FFT_6_6.txt", "CONS_FFT_6_7.txt", "CONS_FFT_6_8.txt", "CONS_FFT_7_4.txt", "CONS_FFT_7_5.txt", "CONS_FFT_7_6.txt", "CONS_FFT_7_7.txt", "CONS_FFT_7_8.txt", "CONS_FFT_8_4.txt", "CONS_FFT_8_5.txt", "CONS_FFT_8_6.txt", "CONS_FFT_8_7.txt", "CONS_FFT_8_8.txt"]"""
#file_list = ["CONS_FFT_16__6_7.txt", "CONS_FFT_18__6_7.txt", "CONS_FFT_20__6_7.txt", "CONS_FFT_22__6_7.txt", "CONS_FFT_24__6_7.txt"]
#file_list = ["BLK_FFT_16__6_7.txt", "BLK_FFT_18__6_7.txt", "BLK_FFT_20__6_7.txt", "BLK_FFT_22__6_7.txt", "BLK_FFT_24__6_7.txt"]
str_gpu_ipc = "gpu_tot_ipc ="
str_gpu_dram_stall = "gpu_stall_dramfull ="
str_L2_MPKI_1 = "Avg_MPKI_Stream1="
str_L2_MPKI_2 = "Avg_MPKI_Stream2="

ipc_dict = {}
dram_dict = {}
mpki_1_dict = {}
mpki_2_dict = {}

for file_i in file_list:
	ipc_list = []
	dram_list = []
	mpki1_list = []
	mpki2_list = []
	f1 = open(file_i, 'r')
	lines = str(f1.read())
	line_list = lines.split("\n")
	for line in line_list:
		if str_gpu_ipc in line:	
			ipc = re.findall("\d+\.\d+", line)
			#print(ipc)
			#print(float(ipc[0]))
			ipc_list.append(float(ipc[0])) #only one IPC is there but findall gives a list of one element
		if str_gpu_dram_stall in line:	
			dram_stall = re.findall("\d+", line)
			#print(dram_stall)
			#print(float(ipc[0]))
			dram_list.append(int(dram_stall[0])) #only one dram_stall is there but findall gives a list of one element
		if str_L2_MPKI_1 in line:	
			mpki1 = re.findall("\d+\.\d+", line)
			#print(mpki1)
			#print(float(ipc[0]))
			if(len(mpki1) != 0):
				mpki1_list.append(float(mpki1[0])) #only one mpki1 is there but findall gives a list of one element
		if str_L2_MPKI_2 in line:	
			mpki2 = re.findall("\d+\.\d+", line)
			#print(mpki2)
			#print(float(ipc[0]))
			if(len(mpki2) != 0):
				mpki2_list.append(float(mpki2[0])) #only one mpki1 is there but findall gives a list of one element
	f1.close()
	#print(dram_list)
	ipc_dict[file_i] = (ipc_list[-1]) 
	dram_dict[file_i] = (dram_list[-1])
	mpki_1_dict[file_i] = (mpki1_list[-1])
	mpki_2_dict[file_i] = (mpki2_list[-1])
#print(ipc_dict)

max_key = max(ipc_dict, key=ipc_dict.get)
print(max_key + " " + str(ipc_dict[max_key]))
print(file_list[-1] + " " + str(ipc_dict[file_list[-1]]))
print("---------------------------------DRAM_STAT-------------------------------");
print(max_key + " " + str(dram_dict.get(max_key)))
print(file_list[-1] + " " + str(dram_dict[file_list[-1]]))
print("---------------------------------MPKI_1_STAT-----------------------------");
print(max_key + " " + str(mpki_1_dict.get(max_key)))
print(file_list[-1] + " " + str(mpki_1_dict[file_list[-1]]))
print("---------------------------------MPKI_2_STAT-----------------------------");
print(max_key + " " + str(mpki_2_dict.get(max_key)))
print(file_list[-1] + " " + str(mpki_2_dict[file_list[-1]]))



