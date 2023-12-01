import snscrape.modules.twitter as sntwitter
import re
from typing import List

from data.dictionaries import stock_tags


class ScrapperContentAuthorDate:
    def __init__(self, profiles_names: List[str], start_date: str, end_date: str):
        self._profiles_names = profiles_names
        self._start_date = start_date
        self._end_date = end_date

    def scrapping_tweets_date_author_content(self) -> List[str]:
        tweets_content = []
        for profile in self._profiles_names:
            query = f"(from:{profile}) until:{self._end_date} since:{self._start_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                tweet_tags = re.findall(r'\$[a-zA-Z]+', tweet.rawContent)
                verified_tweet_tags = list(set([tag for tag in tweet_tags if tag not in stock_tags]))
                if verified_tweet_tags:
                    tweets_content.append([tweet.date,
                                           tweet.user.username,
                                           tweet.rawContent,
                                           verified_tweet_tags])
        return tweets_content
