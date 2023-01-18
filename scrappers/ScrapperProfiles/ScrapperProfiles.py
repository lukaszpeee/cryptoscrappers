from datetime import date
from typing import List
import snscrape.modules.twitter as sntwitter
import re

from data.dictionaries import stock_tags


class ScrapperProfiles:
    def __init__(self, profiles: List[str], since_date: date, until_date: date):
        self._profiles = profiles
        self._since_date = since_date
        self._until_date = until_date

    def start_scrapping_tweets_content(self) -> List[str]:
        tweets_profiles = []
        for profile in self._profiles:
            query = f"(from:{profile}) until:{self._until_date} since:{self._since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweets_profiles.append(tweet.rawContent)
        return tweets_profiles

    def start_scrapping_tweets_date_author_content(self) -> List[str]:
        tweets_content = []
        for profile in self._profiles:
            query = f"(from:{profile}) until:{self._until_date} since:{self._since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweet_tags = re.findall(r'\$[a-zA-Z]+', tweet.rawContent)
                if tweet_tags:
                    verified_tweet_tags = self._remove_stock_tags(tweet_tags)
                else:
                    continue
                if verified_tweet_tags:
                    verified_tweet_tags_no_duplicates = self._remove_duplicates(verified_tweet_tags)
                    tweets_content.append([tweet.date,
                                           tweet.user.username,
                                           tweet.rawContent,
                                           verified_tweet_tags_no_duplicates])
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
        verified_tags = self._remove_stock_tags(extracted_tags)
        return verified_tags

    @staticmethod
    def _remove_stock_tags(list_of_tags: List[str]) -> List[str]:
        upper_list_of_tags = [tag.upper() for tag in list_of_tags]
        return [tag for tag in upper_list_of_tags if tag not in stock_tags]

    @staticmethod
    def _remove_duplicates(list_of_tags: List[str]) -> List[str]:
        return list(set(list_of_tags))
