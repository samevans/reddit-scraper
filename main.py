#! usr/bin/env python3
import config
import praw


reddit = praw.Reddit(client_id=config.APP_CONFIG['client_id'],\
		client_secret=config.APP_CONFIG['client_secret'],\
		user_agent=config.APP_CONFIG['user_agent'],\
		username=config.APP_CONFIG['username'],\
		password=config.APP_CONFIG['password'])


subreddit = reddit.subreddit('hockey')

for submission in subreddit.top(limit=1):
	print(submission.title,submission.id)
