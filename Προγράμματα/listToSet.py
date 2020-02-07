#open file to list

hashtags = []

with open('jneymarjr5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		hashtags.append(currentPlace)

print(len(hashtags))
list_set = set(hashtags)
hashtagsNew = (list(list_set))
print(len(hashtagsNew))