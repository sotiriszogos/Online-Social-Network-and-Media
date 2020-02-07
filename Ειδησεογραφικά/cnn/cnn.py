# first 100 followers of twitter profile


from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth, wait_on_rate_limit=True)

c = 0
list1 = []
hashtags = []
hashtagsall = []

with open('cnnlist3.txt', 'w', encoding="utf-8") as f:
	for user in tweepy.Cursor(api.followers, screen_name="CNN").items():
		if (user.protected == True):
			continue

		if (user.statuses_count < 40):
			continue

		temp = []
		temp1 = []
		temp2 = []
		list1.append(user)
		f.write("%s\n" % user.screen_name)
		c+=1
		if (c > 199):
			break
		end_date = datetime.utcnow() - timedelta(days=180)
		print(c)
		for status in Cursor(api.user_timeline, screen_name=user.screen_name).items():
			temp1 = []
			temp2 = []
			if hasattr(status, "entities"):
				entities = status.entities
				if "hashtags" in entities:
					for ent in entities["hashtags"]:
						if ent is not None:
							if "text" in ent:
								hashtag = ent["text"]
								if hashtag is not None:
									temp.append(hashtag)
									hashtagsall.append(hashtag)
			if status.created_at < end_date:
				temp1 = set(temp)
				temp2 = (list(temp1))
				for hashtag in temp2:
					hashtags.append(hashtag)
				break
		print(len(hashtags))
		print(len(hashtagsall))
          					
for user in list1:
	print(user.screen_name)

print(len(hashtags))  

with open('cnnlist3cleanhashtags.txt', 'w', encoding="utf-8") as g:          				
	for hashtag in hashtags:
		g.write("%s\n" %hashtag)

with open('cnnlist3hashtagsALL.txt', 'w', encoding="utf-8") as o:
	for hashtag in hashtagsall:
		o.write("%s\n" %hashtag)
