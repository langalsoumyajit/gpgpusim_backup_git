import itertools

app_list1 = ["3DS", "BFS2", "BLK", "BP", "CONS", "FFT", "JPEG", "LIB", "LPS", "RAY", "RED", "SAD", "SC", "SCAN", "SCP", "SRAD", "TRD"]

all_combinations = []

for r in range(2,3):
        combinations_object = itertools.combinations(app_list1, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
	

	
