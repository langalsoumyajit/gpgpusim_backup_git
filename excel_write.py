# Writing to an excel
# sheet using Python
import xlwt
import itertools
from xlwt import Workbook

app_list1 = ["3DS", "BFS2", "BLK", "BP", "CFD", "CONS", "FFT", "FWT", "GUPS", "HISTO", "HS", "JPEG", "LIB", "LPS", 
		"LUD", "LUH", "NN", "NW", "RAY", "RED", "SAD", "SC", "SCAN", "SCP", "SRAD", "TRD"]
app_list2 = ["3DS", "BFS2", "BLK"]
all_combinations = []
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet_1')
i = 0
for r in range(2,3):
    combinations_object = itertools.combinations(app_list1, r)
    combinations_list = list(combinations_object)
    all_combinations += combinations_list
for i in range(len(all_combinations)):
    sheet1.write(i, 0, all_combinations[i][0])
    sheet1.write(i, 1, all_combinations[i][1])

wb.save('xlwt example.xls')
