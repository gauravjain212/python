import os
stream = os.popen('date;echo;drbd-overview;echo;tipc-config -n;echo;df -kh;echo;sapcHealthCheck')
output = stream.read()
#print(type(output))
print(output)
newfile = open('newdata','a')
newfile.write(output)
newfile.close()
SC-2:~/test #