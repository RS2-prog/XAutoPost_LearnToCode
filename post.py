import tweepy
import os

consumerKey = os.getenv('TWITTER_CONSUMER_KEY')
consumerSecret = os.getenv('TWITTER_CONSUMER_SECRET')
accessToken = os.getenv('TWITTER_ACCESS_TOKEN')
accessTokenSecret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
bearerToken = os.getenv('TWITTER_BEARER_TOKEN')

def postToX(tweet_text, image_path):
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)

    api = tweepy.API(auth)
    client = tweepy.Client(
        consumer_key=consumerKey,
        consumer_secret=consumerSecret,
        access_token=accessToken,
        access_token_secret=accessTokenSecret)

    media = api.media_upload(filename=image_path)
    client.create_tweet(text=tweet_text, media_ids=[media.media_id])
