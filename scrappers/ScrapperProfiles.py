from datetime import date
from typing import List
from data.dictionaries import profiles
import snscrape.modules.twitter as sntwitter
import re


class ScrapperProfiles:
    def __init__(self, profiles: List, since_date: date, until_date: date):
        self.profiles = profiles
        self.since_date = since_date
        self.until_date = until_date
        self.tweets_profiles = []
        self.extracted_tags = []

    def start_scrapping_tweets(self):
        for profile in self.profiles:
            query = f"(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                self.tweets_profiles.append(tweet.content)

    def start_extracting_tags(self):
        for tweet in self.tweets_profiles:
            matches = re.findall(r'\$[a-zA-Z]+', tweet)
            if matches:
                for match in matches:
                    self.extracted_tags.append(match)  
        
    
        
    