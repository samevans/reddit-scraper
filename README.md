# reddit-scraper
## What is this?
This is a script I wrote to download all the top images off of a selected subreddit. You can define how many you want to look at.

## How do I use it?
In terminal, change directory to where this script is and execute:
```
python3 main.py
```
Select the subreddit and select how many.

You will need to create a file called config.py that specifies the following:
```
APP_CONFIG = {
    'client_id': '',
    'client_secret': '',
    'user_agent': '',
    'username': '',
    'password': ''
}

DIR = '' #The directory you want your images to be downloaded to
```

## Dependencies
- Python 3, I used python 3.7.1
- Gfycat library
- Praw library
```
pip3 install gfycat
```
```
pip3 install praw
```
