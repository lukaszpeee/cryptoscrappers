from datetime import date
from typing import List
from data.dictionaries import profiles
import snscrape.modules.twitter as sntwitter
import re
import pandas as pd


class ScrapperProfiles:
    def __init__(self, profiles: List, since_date: date, until_date: date):
        self.profiles = profiles
        self.since_date = since_date
        self.until_date = until_date

    def start_scrapping_tweets_about(self, tag: str):
        tweets_profiles_about = []
        for profile in self.profiles:
            query = f"(#${tag})(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweets_profiles_about.append([tweet.username, tweet.content])
        df = pd.DataFrame(tweets_profiles_about, columns=['User', 'Tweet'])
        return df