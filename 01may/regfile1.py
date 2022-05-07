import re
email_list = "gaurav <gaurav@example.com>, videha <videha@example.com>, akshara <akshara@example.com>, akshita <akshita@example.com> bobby <bobby@example.com>"

a = re.search("videha", email_list)
print(a)

b = re.search("satish", email_list)
print(b)

c = re.search("bobb[y,i]", email_list)	#Always Provide First Search
print(c)

d = re.search("[g,G]aurav", email_list)
print(d)

e = re.search("[a,A]+", email_list)
print(e)

f = re.search(r"\w+", email_list)
print("value of $f:",f)

h = re.search(r"g[a-z][a-z][a-z][a-z][a-z]",email_list)
print("value of $h",h)

i = re.search(r"g[a-z]{5}",email_list)
print("value of i:", i)

j = re.search(r"g[a-z]+",email_list)
print("value of j:", j)

k = re.search(r"g[A-Za-z]+",email_list)
print("value of k:", k)

l = re.search(r"[A-Za-z]{7}",email_list)
print("value of l:", l)

m = re.search(r"\w+",email_list)
print("value of m:", m)

n = re.search(r"\w+@\w+\.\w+", email_list)
print("value of n:", n)

matched = re.findall(r"\w+@\w+\.\w+", email_list)
print(matched)

match1 = re.finditer(r"\w+@\w+\.\w+", email_list)
print(match1)
next(match1)
