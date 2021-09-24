from config import ConfigFile
import tweepy
import re

c = ConfigFile()

# OAuth setup
auth = tweepy.OAuthHandler(c.config["consumer"]["consumer_key"], c.config["consumer"]["consumer_secret"])
auth.set_access_token(c.config["access"]["access_token"], c.config["access"]["access_token_secret"])
api = tweepy.API(auth)

# Test Twitter authentication
try:
    api.verify_credentials()
    print("\nTwitter Authentication: 200 OK.\n")
except:
    print("\nOops! Error during authentication.\n")

# Obtain username for search
username = input("Give me a username to scrape the last 10 tweets from, for example CNN, BBC, Bloomberg: ")

# Setup API
user_tweets = api.user_timeline(username, count = 10, tweet_mode="extended")

# Append every tweet text to a list
tweet_list = []
for tweet in user_tweets:
    tweets = [[tweet.full_text] for tweet in user_tweets]

# Split inner words of tweet sentances
for tweet_word in tweets:
    tweet_list.append(str(tweet_word).split())

words = []
longest_words = []
shortest_words = []

# Clear words from symbols: #, ', [, @, 2 etc
regex = re.compile('[^a-zA-Z]')
for sentance in tweet_list:
    for word in sentance:
        # Kick out URLS
        word = str(word)
        if word.startswith("https") is False:
            words.append(regex.sub("", word)) 

# Remove duplicate elements and empty strings        
sorted_words = sorted(words, key = len)
sorted_words = list(dict.fromkeys(sorted_words))
sorted_words = list(filter(None, sorted_words))

print("\nFor the last 10 tweets of the user given:")
print("--> Five shortest words are {}".format(sorted_words[0:5]))
print("--> Five longest words from the last 10 post the given user are {}".format(sorted_words[-6:-1]))