import snscrape.modules.twitter as sntwitter
from datetime import date
from typing import List
import pandas as pd


class ScrapperProfile:
    def __init__(self, profile: str, since_date: date, until_date: date):
        self.profile = profile
        self.since_date = since_date
        self.until_date = until_date
        self.tweets_profiles = []

    def start_scrapping_tweets(self):
        query = f"(from:{self.profile}) until:{self.until_date} since:{self.since_date}"
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
            self.tweets_profiles.append([tweet.content])
        df = pd.DataFrame(self.tweets_profiles, columns=['Tweet'])
        print(df)