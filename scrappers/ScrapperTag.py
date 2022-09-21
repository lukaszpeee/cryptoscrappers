from datetime import date
import snscrape.modules.twitter as sntwitter

class ScrapperTag:
    def __init__(self, tagcrypto: str, since_date: date, until_date: date):
        self.tagcrypto = [tagcrypto.upper(), tagcrypto.lower()]
        self.since_date = since_date
        self.until_date = until_date

    def start_counting_tweets(self):
        added_tags = []
        for tag in self.tagcrypto:
            query = f"(${tag}) until:{self.until_date} since:{self.since_date}"
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                added_tags.append(tag)
        return added_tags