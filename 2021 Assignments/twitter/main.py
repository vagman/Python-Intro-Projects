from config import Configuration
import tweepy

con = Configuration()

# OAuth setup
auth = tweepy.OAuthHandler(con.consumer_key, con.consumer_secret)
auth.set_access_token(con.access_token, con.access_token_secret)

api = tweepy.API(auth)

# TODO: Enter user's username to scrape his tweets..
username = input("\nAvailable users for scraping:\n1)Bloomberg\n2)CNBC\n3)NASA\nGive me a username to scrape the last 10 tweets from: ")

users_tweets = api.user_timeline(username, count = 10)
for count, tweet in enumerate(users_tweets):
    print(count, tweet.text)
    tweet_

