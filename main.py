#! usr/bin/env python3
import config
import praw
import requests
import re
import os
from gfycat.client import GfycatClient

reddit = praw.Reddit(client_id=config.APP_CONFIG['client_id'],\
		client_secret=config.APP_CONFIG['client_secret'],\
		user_agent=config.APP_CONFIG['user_agent'],\
		username=config.APP_CONFIG['username'],\
		password=config.APP_CONFIG['password'])

gfycat = GfycatClient()

selected = input("Enter a subreddit: ")

subreddit = reddit.subreddit(selected)
directory = config.DIR+"/"+selected

if not os.path.exists(directory):
    os.makedirs(directory)

howmany = input("How many do you want?: ")

for post in subreddit.top(limit=int(howmany)):
	url = post.url
	breadcrumbs = url.split("/")

	if len(breadcrumbs) == 0:
		file = re.findall("/(.*?)", url)

	file = breadcrumbs[-1]

	if ".gifv" in file:
		continue	

	if "view_video.php" in file:
		continue

	if "." not in file:
		
		if "gfycat" in url:
			gfy = gfycat.query_gfy(file)
			url = gfy['gfyItem']['max5mbGif']
			file += ".gif"
		else:
			continue
			file += ".jpg"

	print(file)
	r = requests.get(url)
	
	with open(os.path.join(directory,file),"wb") as f:
		f.write(r.content)
		size = os.path.getsize(directory+"/"+file)
		
		if size < 600:
			os.remove(directory+"/"+file)
			
