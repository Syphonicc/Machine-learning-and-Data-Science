import tweepy
import textblob
from textblob import TextBlob

API_KEY = '**********'
API_SECRET_KEY = '*******'

Access_Tokken = '*******************************'
Access_Tokken_secret = '********************************'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(Access_Tokken, Access_Tokken_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets('Apple')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

