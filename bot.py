import praw
import time
from credentials import username, password, client_id, client_secret, user_agent
#*****PUT THE PHRASE TO SUMMON YOUR BOT BELOW********
message = "This is an example phrase!!!"
#****************************************************
reddit = praw.Reddit(client_id = client_id, 
				     client_secret = client_secret, 
				     user_agent = user_agent,
				     username = username,
				     password = password)
subreddit = reddit.subreddit("testingground4bots")
print(subreddit)