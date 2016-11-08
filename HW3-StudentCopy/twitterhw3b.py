# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob
import sys
from twitauth import *

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('#AnnArbor')

avsub = 0
avpol = 0
tweetcount = 0
for tweet in public_tweets:                 # reference from https://github.com/praritlamba/Mining-Twitter-Data-for-Sentiment-Analysis
	uprint(tweet.text)
	analysis = TextBlob(tweet.text)
	avpol += (analysis.sentiment.polarity)
	avsub += (analysis.sentiment.subjectivity)
	tweetcount += 1

print("Average subjectivity is ", avsub/tweetcount)
print("Average polarity is ", avpol/tweetcount)