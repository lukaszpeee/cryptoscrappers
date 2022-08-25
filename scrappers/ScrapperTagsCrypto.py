from data.dictionaries import tagscrypto
from datetime import date
from typing import List
import snscrape.modules.twitter as sntwitter
import pandas as pd


class ScrapperTagsCrypto:
    def __init__(self, tagscrypto: List, since_date: date, until_date: date):
        self.tagscrypto = tagscrypto
        self.since_date = since_date
        self.until_date = until_date
        self.tweets_crypto = []
        
    def start_scrapping(self):
        for tag in self.tagscrypto:
            query = f"(#${tag}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                self.tweets_crypto.append([tweet.content])
        df = pd.DataFrame(self.tweets_crypto, columns=['Tweet'])
        print(df)
 
