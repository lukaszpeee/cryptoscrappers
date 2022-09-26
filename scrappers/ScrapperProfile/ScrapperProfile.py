import snscrape.modules.twitter as sntwitter
from datetime import date
from typing import List
import pandas as pd


class ScrapperProfile:
    def __init__(self, profile: str, since_date: date, until_date: date):
        self.profile = profile
        self.since_date = since_date
        self.until_date = until_date

    def start_scrapping_tweets_content(self):
        tweets_profile = []
        query = f"(from:{self.profile}) until:{self.until_date} since:{self.since_date}"
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            tweets_profile.append([tweet.content])
        return tweets_profile
        
    def start_scrapping_tweets_about(self, tag):
        tweets_profiles_about = []
        query = f"(#${tag})(from:{self.profile}) until:{self.until_date} since:{self.since_date}"
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            tweets_profiles_about.append([tweet.content])
        return tweets_profiles_about
