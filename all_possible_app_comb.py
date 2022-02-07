
app_list1 = ["3DS", "BFS2", "BLK", "BP", "CFD", "CONS", "FFT", "FWT", "GUPS", "HISTO", "HS", "JPEG", "LIB", "LPS", 
		"LUD", "LUH", "NN", "NW", "RAY", "RED", "SAD", "SC", "SCAN", "SCP", "SRAD", "TRD"]
app_list2 = ["3DS", "BFS2", "BLK", "BP", "CFD", "CONS", "FFT", "FWT", "GUPS", "HISTO", "HS", "JPEG", "LIB", "LPS", 
		"LUD", "LUH", "NN", "NW", "RAY", "RED", "SAD", "SC", "SCAN", "SCP", "SRAD", "TRD"]
app_comb = ""

for app1 in app_list1:
	for app2 in app_list2:
		if app1 != app2:
			app_comb = app1 + "_" + app2
			print(app_comb)
	

	
