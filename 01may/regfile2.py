import re

resultcode = open("sapclog",'r')
resultcodes = resultcode.read()

#matched = re.search(r"Result-Code: \d+", resultcodes)
#print(matched)

matched1 = re.findall(r"Result-Code: \d+", resultcodes)
print(matched1)

resultcode.close()

orc = open("orcfile",'w')
for item in matched1:
	orc.write(item + "\n")
orc.close()
