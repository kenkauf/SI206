# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.


# print("""No output necessary although you 
# 	can print out a success/failure message if you want to.""")

import tweepy
from twitauth import *            # Store sensative private info in different file

print('\nKennedy Kaufman // 61371023\n\n\n')

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)  #authenication

api = tweepy.API(auth)

fname = 'C:/Users/kenka/Desktop/Photos/murrayintree.jpg' # image location
message = '#UMSI-206 #Proj3'                              # message to be posted
try:
	api.update_with_media(filename=fname, status=message) # API Reference: http://docs.tweepy.org/en/v3.5.0/api.html
	print("Done")
except:
	print("Unable to post")                        # if failed, prompt user