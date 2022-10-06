f1 = open("articles", 'rb')
f2 = open("References", 'rb')
fo = open("tree.csv", "w", encoding = "utf-8")

all = []
alldic = {}
for l in f1:
	all.append(l.decode("utf-8").split("\n")[0])
	alldic[l.decode("utf-8").split("\n")[0]] = []

cnt = 0
for l in f2:
	l = l.decode("utf-8").split("\n")[0]
	# l = l.split(";")
	# fo.write(all[cnt] + ",")
	for i in all:
		if i in l:
			alldic[i].append(all[cnt])
	cnt += 1

for i in alldic:
	fo.write(i + ",\"")
	for j in alldic[i]:
		fo.write(j + ",")
	fo.write("\"\n")

f1.close()
f2.close()
fo.close()