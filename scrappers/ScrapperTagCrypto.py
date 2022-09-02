from datetime import date
from typing import List
import snscrape.modules.twitter as sntwitter
import pandas as pd


class ScrapperTagCrypto:
    def __init__(self, tagcrypto: str, since_date: date, until_date: date):
        self.tagcrypto = [tagcrypto.upper(), tagcrypto.lower()]
        self.since_date = since_date
        self.until_date = until_date
        self.tweets_crypto = []
        
    def start_scrapping_tweets(self):
        for tag in self.tagcrypto:
            query = f"(${tag}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                self.tweets_crypto.append(tweet.content)