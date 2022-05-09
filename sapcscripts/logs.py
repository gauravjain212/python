import os
stream = os.popen('ls -lrth')
output = stream.readlines()
print(type(output))
print(output)