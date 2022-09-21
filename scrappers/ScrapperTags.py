from data.dictionaries import tagscrypto
from datetime import date
from typing import List
import snscrape.modules.twitter as sntwitter


class ScrapperTags:
    def __init__(self, tagscrypto: List, since_date: date, until_date: date):
        self.tagscrypto = [x.lower() for x in tagscrypto] + [x.upper() for x in tagscrypto]
        self.since_date = since_date
        self.until_date = until_date
        
    def start_adding_tags(self):
        added_tags = []
        for tag in self.tagscrypto:
            query = f"(${tag}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                added_tags.append(tag)
        return added_tags