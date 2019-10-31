#!/usr/bin/env python
# coding: utf-8

# In[13]:


import sys
sys.path.insert(0, 'C:/Users/Aaron/Documents')

# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
from config import TW_consumer_key, TW_consumer_skey, TW_access_token, TW_access_stoken, OW_api_key


# In[14]:


# # Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(TW_consumer_key, TW_consumer_skey)
auth.set_access_token(TW_access_token, TW_access_stoken)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[15]:


# Weather API Key
weather_k= OW_api_key


# In[16]:


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
    auth = tweepy.OAuthHandler(TW_consumer_key, TW_consumer_skey)
    auth.set_access_token(TW_access_token, TW_access_stoken)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the weather
    api.update_status(
        "Weather in Washington, DC at " +\
        (datetime.datetime.now().strftime("%I:%M %p") + " is " +\
         str(weather_json["main"]["temp"])+"F"))

    # Print success message


# In[ ]:


# Set timer to run every 1 hour
while(True):
    WeatherTweet()
    time.sleep(3600)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




