import tweepy

# Set up your Twitter API credentials
consumer_key = "API_consumer_key"
consumer_secret = "API_consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing the keyword
keyword = "keyword" #change "keyword" by the keyword you want to delete tweets containing this keyword  
tweets = api.user_timeline(count=1000) #This will load your 1000 last tweets you can change it

# Iterate through the tweets and delete those that contain the keyword
for tweet in tweets:
    if keyword in tweet.text:
        api.destroy_status(tweet.id)
