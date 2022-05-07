myfile = open('/root/python/testfile.txt')

#print(myfile.read())
lines = myfile.readlines()
print(type(lines))
print(lines)
for line1 in lines:
	print(line1.strip())

myfile.close()