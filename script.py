import subprocess
import os
import sys
import re

#------------------------------- Invalid number of argument checker------------------------
if(len(sys.argv) == 5):
	print("Good to go")
elif(len(sys.argv) == 3):
	exit("ERROR !!!! : Please enter initial CTA values")
else:
	exit("ERROR !!!! : Please enter two applications name with a space in between and initial CTAs")
#------------------------------------------------------------------------------------------

#-------------------------------It will create the file list-------------------------------
cta_num0 = int(sys.argv[3])
cta_num1 = int(sys.argv[4])
app1 = sys.argv[1]
app2 = sys.argv[2]
file_name = ""
file_list = []
print(app1 + " " + app2)
for i in range(cta_num0,5):
	for j in range(cta_num1,9):
		file_name = app1 + "_" + app2 + "_" + str(i) + "_" + str(j) + ".txt"
		file_list.append(file_name)
#print(file_list)
#------------------------------------------------------------------------------------------


#file_list = ["CFD_3DS_15__6_7.txt", "CFD_3DS_14_4_8.txt", "CFD_3DS_21__6_7.txt", "CFD_3DS_24__6_7.txt"]
#file_list = ["BP_FFT_15__6_7.txt", "BP_FFT_14_4_8.txt", "BP_FFT_21__6_7.txt", "BP_FFT_24__6_7.txt"]
#---------------------------------Change file name----------------------------------------------------------------------
"""file_list = ["BP_FFT_4_4.txt", "BP_FFT_4_5.txt", "BP_FFT_4_6.txt", "BP_FFT_4_7.txt", "BP_FFT_4_8.txt", "BP_FFT_5_4.txt", "BP_FFT_5_5.txt", "BP_FFT_5_6.txt", "BP_FFT_5_7.txt", "BP_FFT_5_8.txt", "BP_FFT_6_4.txt", "BP_FFT_6_5.txt", "BP_FFT_6_6.txt", "BP_FFT_6_7.txt", "BP_FFT_6_8.txt", "BP_FFT_7_4.txt", "BP_FFT_7_5.txt", "BP_FFT_7_6.txt", "BP_FFT_7_7.txt", "BP_FFT_7_8.txt", "BP_FFT_8_4.txt", "BP_FFT_8_5.txt", "BP_FFT_8_6.txt", "BP_FFT_8_7.txt", "BP_FFT_8_8.txt"]
#file_list = ["BP_FFT_16__6_7.txt", "BP_FFT_18__6_7.txt", "BP_FFT_20__6_7.txt", "BP_FFT_22__6_7.txt", "BP_FFT_24__6_7.txt"]"""

#----------------------------Initialized the CTA-------------------------------------------------------------------------
str_gpu0 = "-gpgpu_shader_cta_app0"
str_gpu1 = "-gpgpu_shader_cta_app1"

str_write0 = "-gpgpu_shader_cta_app0" + " " + str(cta_num0)
str_write1 = "-gpgpu_shader_cta_app1" + " " + str(cta_num1)
f2 = open("gpgpusim.config", 'r')
lines = str(f2.read())
line_list = lines.split("\n")

f9 = open("gpgpusim.config", 'w')
f9.write(line_list[0])
for line in line_list[1:]:
	
	if str_gpu0 in line:	
		f9.write("\n" + str_write0)
	else:
		f9.write("\n" + line)
f9.close()
f8 = open("gpgpusim.config", 'w')
f8.write(line_list[0])
for line in line_list[1:]:
	if str_gpu1 in line:	
		f8.write("\n" + str_write1)
	else:
		f8.write("\n" + line)
f8.close()	
f2.close()
#f3.close()	
dyn_command = "./gpgpu_ptx_sim__mergedapps -apps" + " " + app1 + " " + app2
#------------------------------------------------------------------------------------------------------------------------
for file_i in file_list:
	#f1 = open(file_i, 'w')	
	str_write0 = "-gpgpu_shader_cta_app0" + " " + str(cta_num0)
	str_write1 = "-gpgpu_shader_cta_app1" + " " + str(cta_num1)
	
	#--------------write CTA0 in config file-----------------------------------------
	f5 = open("gpgpusim.config", 'r')
	lines = str(f5.read())
	line_list = lines.split("\n")
	f10 = open("gpgpusim.config", 'w')
	f10.write(line_list[0])
	for line in line_list[1:]:
		if str_gpu0 in line:	
			f10.write("\n" + "-gpgpu_shader_cta_app0" + " " + str(cta_num0))
			#print(f6.write(str_write0 + "\n"))
		else:
			f10.write("\n" + line)
	f10.close()
	f5.close()

	#--------------write CTA1 in config file-----------------------------------------
	f12 = open("gpgpusim.config", 'r')
	lines = str(f12.read())
	line_list = lines.split("\n")
	f11 = open("gpgpusim.config", 'w')
	f11.write(line_list[0])
	for line in line_list[1:]:
		if str_gpu1 in line:	
			f11.write("\n" + str_write1)
		else:
			f11.write("\n" + line)
	f11.close()
	f12.close()
	
	#----------------write logs in output file------------------------------------------------------------------------	
	f1 = open(file_i, 'w')	
	if (cta_num1 <= 8) and (cta_num0 <= 8) :
		#---------------------------------------------------------------------------------------------------------
		#x = subprocess.Popen(['./gpgpu_ptx_sim__mergedapps -apps BP FFT'], shell=True, stdout=f1)
		x = subprocess.Popen([dyn_command], shell=True, stdout=f1)
		#---------------------------------------------------------------------------------------------------------
		x.wait()
		f1.close()
		#dyn_command = "./gpgpu_ptx_sim__mergedapps -apps MM BLK" + " > " + file_i
		#os.system(dyn_command)
		f4 = open(file_i, 'a')
		f4.write("\n"+str(cta_num0))
		f4.write("\n"+str(cta_num1))
		cta_num1 = cta_num1 + 1
		f4.close()	

	if (cta_num0 < 8) and (cta_num1 == 9) :
		cta_num0 = cta_num0 + 1
		#print(cta_num0)
		cta_num1 = 4
	
	#fl.close()	
		
	
	#os.system("Finished for SM " + str(sm_num - 3))
#=====================================================================================================================================
#-------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------Finding out best possible CTA combination---------------------------------------------------
str_gpu_ipc = "gpu_tot_ipc ="

ipc_dict = {}

for file_i in file_list:
	ipc_list = []
	f13 = open(file_i, 'r')
	lines = str(f13.read())
	line_list = lines.split("\n")
	for line in line_list:
		if str_gpu_ipc in line:	
			ipc = re.findall("\d+\.\d+", line)
			#print(float(ipc[0]))
			ipc_list.append(float(ipc[0]))
	f13.close()
	#print(ipc_list)
	ipc_dict[file_i] = (ipc_list[-1]) 
#print(ipc_dict)
max_key = max(ipc_dict, key=ipc_dict.get)
print(max_key + " " + str(ipc_dict[max_key]))
print(file_list[-1] + " " + str(ipc_dict[file_list[-1]]))
#------------------------------------------------------------------------------------------------------------------------------------

	
