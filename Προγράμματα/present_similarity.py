hashtagsForName1 = []
hashtagsForName2 = []

def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return float(len(s1.intersection(s2))) / len(s1.union(s2))

with open('name1allhashtags.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		hashtagsForName1.append(currentPlace)

with open('name2allhashtags.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		hashtagsForName2.append(currentPlace)

k = jaccard_similarity(hashtagsForName1, hashtagsForName2)
print("Jaccard similarity is: ", k)