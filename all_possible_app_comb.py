import itertools

app_list1 = ["BLK", "BP", "CFD", "CONS", "FFT", "JPEG", "LIB", "LPS", "MM", "NW", "SAD", "SCP", "TRD"]

all_combinations = []

for r in range(2,3):
        combinations_object = itertools.combinations(app_list1, r)
        combinations_list = list(combinations_object)
        all_combinations += combinations_list
print(all_combinations)	

	
