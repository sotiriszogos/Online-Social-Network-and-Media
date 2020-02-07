hashtags = []

with open('hashtags.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		hashtags.append(currentPlace)

hashtags = list(set(hashtags))
print(len(hashtags))
