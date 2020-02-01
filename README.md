## JimBot

The purpose of this bot is to track a subreddit and reply with user specified images when prompted by a user. 

### Dependencies
>PRAW: [Documentation](https://praw.readthedocs.io/en/latest/), [Github](https://github.com/praw-dev/praw)

### Installation

Clone this repo 

```
git clone https://github.com/mjangle1985/jimbot
```

Install PRAW to your local system from [here](https://github.com/praw-dev/praw)

### Setting up the bot

Make a file ./credentials/credentials.py and copy the contents of credentialsExample.py with your appropriate reddit credentials

You can find out more about reddit oAuth [here](https://github.com/reddit-archive/reddit/wiki/oauth2).

place a url list of images you'd like the bot to reply randomly with. Note you must place each url in a separate line. 
