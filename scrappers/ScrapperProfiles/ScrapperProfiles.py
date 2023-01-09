from datetime import date
from typing import List
import snscrape.modules.twitter as sntwitter
import re


class ScrapperProfiles:
    def __init__(self, profiles: List, since_date: date, until_date: date):
        self.profiles = profiles
        self.since_date = since_date
        self.until_date = until_date

    def start_scrapping_tweets_content(self) -> List[str]:
        tweets_profiles = []
        for profile in self.profiles:
            query = f"(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweets_profiles.append(tweet.content)
        return tweets_profiles

    def start_scrapping_tweets_date_author_content(self) -> List[str]:
        tweets_content = []
        for profile in self.profiles:
            query = f"(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweet_tags = re.findall(r'\$[a-zA-Z]+', tweet.content)
                if tweet_tags:
                    tweets_content.append([tweet.date,
                                           tweet.user.username,
                                           tweet.content,
                                           [x.upper() for x in tweet_tags]])
                else:
                    continue
        return tweets_content

    def start_extracting_tags(self, tweets_profiles: List[str]) -> List[str]:
        extracted_tags = []
        for tweet in tweets_profiles:
            matches = re.findall(r'\$[a-zA-Z]+', tweet)
            if matches:
                for match in matches:
                    extracted_tags.append(match)
        return extracted_tags

    @staticmethod
    def remove_stock_tags(list_of_tags: List[str], list_of_stock_tags: List[str]) -> List[str]:
        return [tag for tag in list_of_tags if tag not in list_of_stock_tags]
