oldfile = open('/root/python/newdata','a')

oldfile.write("mynetworks\n")

oldfile.close()

myfile = open('/root/python/newdata','r')

print(myfile.readlines())

myfile.close()
