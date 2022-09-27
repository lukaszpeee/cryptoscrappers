from datetime import date
from typing import List
import snscrape.modules.twitter as sntwitter
import re


class ScrapperProfiles:
    def __init__(self, profiles: List, since_date: date, until_date: date):
        self.profiles = profiles
        self.since_date = since_date
        self.until_date = until_date

    def start_scrapping_tweets_content(self):
        tweets_profiles = []
        for profile in self.profiles:
            query = f"(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweets_profiles.append(tweet.content)
        return tweets_profiles

    def start_scrapping_tweets_date_author_content(self):
        tweets_profiles = []
        for profile in self.profiles:
            query = f"(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweets_profiles.append([tweet.date, tweet.user.username, tweet.content])
        return tweets_profiles

    def start_scrapping_tweets_about_tag(self, tag: str):
        tweets_profiles_about_tag = []
        for profile in self.profiles:
            query = f"(#${tag})(from:{profile}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweets_profiles_about_tag.append(tag)
        return tweets_profiles_about_tag

    def start_extracting_tags(self, tweets_profiles: List):
        extracted_tags = []
        for tweet in tweets_profiles:
            matches = re.findall(r'\$[a-zA-Z]+', tweet)
            if matches:
                for match in matches:
                    extracted_tags.append(match)
        return extracted_tags
