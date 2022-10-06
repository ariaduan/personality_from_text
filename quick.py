f1 = open("Title2","rb")
f2 = open("Title1","rb")
fo = open("Title3",'w',encoding = "utf-8")

all = []
b = []
c = 0
for l in f1:
	if c == 13627:
		break
	all.append(l.decode("utf-8"))
	c += 1


for l in f1:
	b.append(l.decode("utf-8"))

cnt = 0
for l in f2:
	if l.decode("utf-8") in all:
		fo.write(l.decode("utf-8"))
	elif l.decode("utf-8") in b:
		fo.write("x\n")
	else:
		fo.write("\n")
		cnt += 1
print(cnt)
f1.close()
f2.close()
fo.close()