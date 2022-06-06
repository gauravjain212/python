import re
from operator import itemgetter
inline = r"Chandiwali_sapclogs_test"

important = []

ER_Data = ["ER"]

with open(inline) as f:
    f = f.readlines()

for line in f:
    for ER in ER_Data:
        if ER in line:
            important.append(line)
            break
#print(important)

for sessionid in important:
    str_1 = sessionid.split()
#    print(str_1)
    print(*itemgetter(9,11)(str_1))

#sessionid = important[0]
#print(sessionid)
#print(important[0])
#print(important[1])

