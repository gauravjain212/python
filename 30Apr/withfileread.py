with open ("newdata",'r') as myfile:
	for line in myfile.readlines():
		print(line.strip())
