from data.dictionaries import tagscrypto
from raports.Raport import Raport
from scrappers.ScrapperTags.ScrapperTags import ScrapperTags


def main_scrapper_tags():
    scrapper_tags = ScrapperTags(tagscrypto, '2022-01-01', '2022-01-31')
    scrapped_tags = scrapper_tags.start_adding_tags()
    scrapper_profiles_raport = Raport('Styczen', scrapped_tags, f'{path}/raport_scrapper_tags_styczen.xlsx')
    scrapper_profiles_raport.create_raport()
