from datetime import date
from typing import List
from dictionaries import profiles
import snscrape.modules.twitter as sntwitter
import pandas as pd


class ScrapperProfiles:
    def __init__(self, profiles: List, since_date: date, until_date: date):
        self.profiles = profiles
        self.since_date = since_date
        self.until_date = until_date
        self.tweets_profiles = []

    def start_scrapping(self):
        for profile in self.profiles:
            query = f"(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                self.tweets_profiles.append([tweet.content])
        df = pd.DataFrame(self.tweets_profiles, columns=['Tweet'])
        print(df)
    
        
    