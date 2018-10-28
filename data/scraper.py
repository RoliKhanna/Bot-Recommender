import tweepy
import json

credentials = {}

with open ("permission.json", "r") as readFile:
    credentials = json.load(readFile)

auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])

api = tweepy.API(auth)

tweets = api.user_timeline("year_progress")

with open ("/Users/sandeepkhanna/Desktop/Fun/Bot_Recommender/data/raw/sampleTweets.json", "a") as writeFile:
    for tweet in tweets:
        writeFile.write('%s\n' %tweet)
