newfile = open('/root/python/newdata','w')

newfile.write("Here\n is new\n file to\n create\n")

newfile.close()

myfile = open('/root/python/newdata','r')

print(myfile.readlines())

myfile.close()
