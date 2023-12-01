from typing import List
import snscrape.modules.twitter as sntwitter
import re

from snscrape.base import ScraperException
from tqdm import tqdm

from data.dictionaries import stock_tags


class ScrapperContent:
    def __init__(self, profiles_names: List[str], start_date: str, end_date: str):
        self._profiles_names = profiles_names
        self._start_date = start_date
        self._end_date = end_date

    def scrapping_tweets_content(self) -> List[str]:
        tweets_profiles = []
        for profile in tqdm(self._profiles_names, desc='Scraping profiles'):
            query = f"(from:{profile}) until:{self._end_date} since:{self._start_date}"
            try:
                print(f"Scrapping profile: {profile}")
                for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                    tweets_profiles.append(tweet.rawContent)
            except ScraperException:
                print(f"There was a problem during scrapping {profile}'s tweets.")
        return tweets_profiles

    @staticmethod
    def extracting_tags(tweets_profiles: List[str]) -> List[str]:
        extracted_tags = []
        for tweet in tweets_profiles:
            matches = re.findall(r'\$[a-zA-Z]+', tweet)
            for match in matches:
                if match not in stock_tags:
                    extracted_tags.append(match)
        return extracted_tags