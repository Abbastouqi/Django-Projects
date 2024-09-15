import tweepy
import facebook
from googleapiclient.discovery import build
from pytrends.request import TrendReq

def get_twitter_trends(api_key, api_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    trends = api.get_place_trends(1)  # 1 is the woeid for worldwide
    return trends[0]['trends']

def get_facebook_trends(access_token):
    graph = facebook.GraphAPI(access_token)
    trends = graph.get_object('search?type=topic&q=')
    return trends['data']

def get_google_trends():
    pytrends = TrendReq()
    trending_searches_df = pytrends.trending_searches(pn='united_states')
    return trending_searches_df[0].tolist()