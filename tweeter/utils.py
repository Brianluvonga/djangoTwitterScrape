from .models import TweeterScraper
import GetOldTweets3 as got


def scrape_tweets(username, start_date, end_date):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setSince(start_date).setUntil(end_date).setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for tweet in tweets:
        t = TweeterScraper(username=tweet.username, tweet_text=tweet.text, tweet_date=tweet.date, tweet_link=tweet.permalink)
        t.save()
    return tweets
