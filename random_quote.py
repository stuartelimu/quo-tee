# tweet random quote
import os
from os.path import join, dirname
from dotenv import load_dotenv

import requests

import tweepy

api_url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_quote():
    headers = {
        'x-rapidapi-host': "andruxnet-random-famous-quotes.p.rapidapi.com",
        'x-rapidapi-key': "a479f45ademsh34f4853b72cf3a0p16295cjsnc21486913d86",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
    }
    response = requests.get(api_url, headers=headers)
    json = response.json()[0]
    tweet = json['quote'] + " - " + json['author']
    return tweet

def tweet_quote():
    tweet = get_quote()
    status = api.update_status(tweet)
    print(status.id)

tweet_quote()
