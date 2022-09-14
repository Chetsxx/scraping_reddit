import json
import pandas as pd
import matplotlib.pyplot as plt
import praw

client_id = "YOUR CLIENT ID"
client_secret =	'YOUR SECRET KEY'
password = 'YOUR PASSWORD'
user_agent = 'YOUR APP NAME'
username = 'YOUR USERNAME'


reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username,
)

data = []

subreddit = reddit.subreddit("LearnJapanese")

top = subreddit.top(limit=100)
for sub in top:
    post = dict()

    submission = reddit.submission(sub)

    post['title'] = submission.title
    post['flair'] = submission.link_flair_text
    post['score'] = submission.score
    post['upvote_to_vote'] = submission.upvote_ratio
    post['comments'] = submission.num_comments

    data.append(post)

with open('top100.json', 'w') as f:
    json.dump(data, f)

with open('top100.json', 'r') as f:
    data = json.load(f)




