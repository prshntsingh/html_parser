import re

path = "/home/prashant/parser/blog.html"  //path to file to be parsed
f = open(path,'r')
s=f.read()
f.close()
empty = []
count = {}
level = {}
stack =[]

alltagsregx = re.compile(r'<(/?\w+)') #takes all opening and closing tags closing tabs with '\'
opentagsregx = re.compile(r'<(\w+)')
closetagsregx =re.compile(r'</(\w+)')

alltags = alltagsregx.findall(s)
opentags = opentagsregx.findall(s)
closetags = closetagsregx.findall(s)

#updating the empty list
for i in set(opentags):
	if i not in set(closetags):
		empty.append(i)

for i in opentags:
	if i not in count.keys():
		count[i] = 1
	else:
		count[i] = count[i]+1


for i in alltags:
	if i not in empty:
		if i[0]!='/':
			stack.append(i)
			# lev[i]=str(len(stack))
			if i in level.keys():
				level[i]=level[i]+","+str(len(stack))
			else:
				level[i]=str(len(stack))
		else:
			stack.pop()
print("Tag and their respective levels:-")
for i in level:
	print(i+"\t\t"+level[i])
print("\n\n\n--------------------------------------------------------------------------------")
print("\+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n\n\nTag and their respective counts:-")
for i in count:
	print(i+"\t\t"+str(count[i]))
print("\n\n\n--------------------------------------------------------------------------------")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("empty tags are")
print(empty)

