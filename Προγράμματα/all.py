

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2))) / len(s1.union(s2))

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
listAll = []

with open('jneymarjr5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list1.append(currentPlace)

listAll.append(list1)

with open('mbaplist3hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list2.append(currentPlace)

listAll.append(list2)

with open('BorisJohnson5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list3.append(currentPlace)

listAll.append(list3)

with open('jeremycorbyn5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list4.append(currentPlace)

listAll.append(list4)

with open('BBCWorld5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list5.append(currentPlace)

listAll.append(list5)

with open('cnnlist3hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list6.append(currentPlace)

listAll.append(list6)

with open('muse5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list7.append(currentPlace)

listAll.append(list7)

with open('PLACEBOWORLD5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		list8.append(currentPlace)

listAll.append(list8)

finalarr = []

for l in listAll:
	new = []
	for m in listAll:
		k=jaccard_similarity(l,m)
		new.append(k)
	finalarr.append(new)

print("         neymar  mbappe   boris  corbyn    bbc      cnn    muse    placebo")

names = ["neymar", "mbappe", "boris ", "corbyn", "bbc   ", "cnn   ", "muse  ", "placebo"]

for i in range(0,len(listAll)):
	t=""
	t=t+names[i]
	for j in range(0,len(listAll)):
		t = t + "    " + str(round(finalarr[i][j],3))
	print(t)


