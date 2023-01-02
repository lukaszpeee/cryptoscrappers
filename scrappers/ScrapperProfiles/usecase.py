from pandas import DataFrame

from data.dictionaries import profiles, profiles_tests
from raports.FullContentRaport import FullContentRaport
from raports.TagRaport import TagRaport
from scrappers.ScrapperProfiles.ScrapperProfiles import ScrapperProfiles


def main_scrapper_profiles_for_month(path: str) -> DataFrame:
    scrapper_profiles = ScrapperProfiles(profiles, '2022-12-01', '2022-12-31')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_content()
    extraced_tags = scrapper_profiles.start_extracting_tags(scrapped_tweets)
    scrapper_profiles_raport = TagRaport('Listopad', extraced_tags, f'{path}/raport_tags_grudzien.xlsx')
    scrapper_profiles_raport.create_tag_raport()


def main_scrapper_tweets_date_author_content_for_month(path: str) -> DataFrame:
    scrapper_profiles = ScrapperProfiles(profiles_tests, '2022-12-01', '2022-12-31')
    tweets_date_author_content = scrapper_profiles.start_scrapping_tweets_date_author_content()
    tweets_date_author_content_raport = FullContentRaport('Listopad', tweets_date_author_content,
                                                          f'{path}/raport_full_grudzien.xlsx')
    tweets_date_author_content_raport.create_full_content_raport()

