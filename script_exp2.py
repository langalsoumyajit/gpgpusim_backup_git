import subprocess
import os
import sys
import re
import shutil


app_list1 = ["BLK", "BP", "CFD", "CONS", "FFT", "FWT", "GUPS", "HISTO", "HS", "JPEG", "LIB", "LPS"]
app_list2 = ["LUD", "LUH", "NN", "NW", "QTC", "RAY", "RED", "SAD", "SC", "SCAN", "SCP", "SRAD", "TRD"]
file_name = ""
source_dir = '/home/soumyajit/gpgpusim-3.2.2/mafia3/pthread_benchmark'
target_dir = '/home/soumyajit/gpgpusim-3.2.2/mafia3/pthread_benchmark/Results_5k'

for app1 in app_list1:
	for app2 in app_list2:
		dyn_command = "./gpgpu_ptx_sim__mergedapps -apps" + " " + app1 + " " + app2
		file_name = app1 + "_" + app2 + "4_4_5k.txt" 
		f1 = open("/home/soumyajit/gpgpusim-3.2.2/mafia3/pthread_benchmark/Results_5k/" + file_name, 'w')	
		x = subprocess.Popen([dyn_command], shell=True, stdout=f1)
		x.wait()
		f1.close()
		#shutil.move(os.path.join(source_dir, file_name), target_dir)
	

	
