#!/usr/bin/env python
# coding: utf-8



import sys
sys.path.insert(0, 'C:/Users/Aaron/Documents')

# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime

consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")
weather_api_key = os.environ.get("weather_api_key")




# # Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())





# Weather API Key
weather_k= weather_api_key





# Create a function that gets the weather in London and Tweets it

def WeatherTweet():

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Washington, D.C."
    units = "imperial"
    query_url = url + "appid=" + weather_k + "&q=" + city + "&units=" + units

    # Perform the API call to get the weather
    weather_response = req.get(query_url)
    weather_json = weather_response.json()
    print(weather_json)

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "Weather in Washington, DC at " +\
        (datetime.datetime.now().strftime("%I:%M %p") + " is " +\
         str(weather_json["main"]["temp"])+"F"))





# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(3600)




