import subprocess
for i in range(2):
	subprocess.run(['pwd'], shell=True)
	subprocess.run(['ls'], shell=True)
	i = i + 1
