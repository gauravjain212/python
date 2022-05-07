with open ('newdata','a') as myfile:
	myfile.write("one more line\n")
	print(myfile.readlines())
