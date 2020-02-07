#jaccard similarity

import numpy as np
from sklearn.metrics import jaccard_score

hashtagscnn = []
hashtagsmbap = []

def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

with open('BorisJohnson5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		hashtagscnn.append(currentPlace)

list_set_cnn = set(hashtagscnn)
hashtagsCN = (list(list_set_cnn))

with open('jeremycorbyn5hashtagsALL.txt', 'r', encoding="utf8") as filehandle:
	for line in filehandle:
		currentPlace = line[:-1]
		hashtagsmbap.append(currentPlace)

list_set_mb = set(hashtagsmbap)
hashtagsMba = (list(list_set_mb))

k = jaccard_similarity(hashtagscnn, hashtagsmbap)
print("Jaccard similarity is: ", k)