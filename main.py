#! usr/bin/env python3
import config
import praw
import requests
import re
import os


reddit = praw.Reddit(client_id=config.APP_CONFIG['client_id'],\
		client_secret=config.APP_CONFIG['client_secret'],\
		user_agent=config.APP_CONFIG['user_agent'],\
		username=config.APP_CONFIG['username'],\
		password=config.APP_CONFIG['password'])


input = input("Enter a subreddit: ")
subreddit = reddit.subreddit(input)

directory = config.DIR+"/"+input
if not os.path.exists(directory):
    os.makedirs(directory)

subreddit = reddit.subreddit(input)
for post in subreddit.top(limit=500):
	url = post.url
	breadcrumbs = url.split("/")

	if len(breadcrumbs) == 0:
		file = re.findall("/(.*?)", url)

	file = breadcrumbs[-1]

	
	if "." not in file:
		continue
		print(url)
		print(file)
		if "gfycat" in url:
			file += ".mp4"
			url = "https://giant.gfycat.com/"
		else:
			file += ".jpg"

	print(file)
	r = requests.get(url)

	with open(os.path.join(directory,file),"wb") as f:
		f.write(r.content)
