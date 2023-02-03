import tweepy
from django.shortcuts import render
from .models import TweeterScraper

def fetch_tweets(request):
    # Twitter API credentials
    consumer_key = 'your consumer key'
    consumer_secret = 'your consumer secret'
    access_token = 'your access token'
    access_secret = 'your access secret'

    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    # Fetch tweets from specific user
    tweets = api.user_timeline(screen_name='elonmusk', count=200)

    # Store tweets in the database
    for tweet in tweets:
        t = TweeterScraper(username=tweet.user.screen_name, tweet_text=tweet.text, tweet_date=tweet.created_at, tweet_link = tweet.id)
        t.save()

    return render(request, 'tweets.html', {'tweets': tweets})
