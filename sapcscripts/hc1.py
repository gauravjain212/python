import os

stream = os.popen('date;sh\r\nls')

output = stream.read()

print(output)

newfile = open('newdata1','a')

newfile.write(output)

newfile.close()
