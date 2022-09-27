import pandas as pd

from data.dictionaries import profiles_tests, profiles
from data.raports import raport_01, raport_02, raport_03, raport_04, raport_05, raport_06, raport_07, raport_08
from raports.MergedRaport import MergedRaport
from raports.Raport import Raport
from raports.VerificationMergedRaport import VeriticationFirstAndLast, VeriticationFirstThreeMonths, \
    VeriticationLastFreeMonths, VeriticationAllMonths
from scrappers.ScrapperProfiles.ScrapperProfiles import ScrapperProfiles


def main_scrapper_profiles():
    scrapper_profiles = ScrapperProfiles(profiles_tests, '2022-08-01', '2022-08-07')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_content()
    extraced_tags = scrapper_profiles.start_extracting_tags(scrapped_tweets)
    scrapper_profiles_raport = Raport('Sierpien', extraced_tags, f'{path}/raport_test2.xlsx')
    scrapper_profiles_raport.create_raport()
    
    raports = [raport_01, raport_02, raport_03, raport_04, raport_05, raport_06, raport_07, raport_08]
    new_raport = MergedRaport(raports, f'{path}/completed_raport.xlsx')
    
    merged_raports = new_raport.merge_raports('Tag')
    
    ver_fal = VeriticationFirstAndLast(merged_raports)
    ver_fal = ver_fal.make_verivication()
    
    ver_ftm = VeriticationFirstThreeMonths(ver_fal)
    ver_ftm = ver_ftm.make_verivication()
    
    ver_ltm = VeriticationLastFreeMonths(ver_ftm)
    ver_ltm = ver_ltm.make_verivication()
    
    ver_all = VeriticationAllMonths(ver_ltm)
    ver_all = ver_all.make_verivication
    ver_all.to_excel(f'{path}/test_verification_merged_raport.xlsx')


def main_scrapper_profiles_content_and_author():
    scrapper_profiles = ScrapperProfiles(profiles, '2022-01-01', '2022-01-31')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_styczen')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-02-01', '2022-01-28')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_luty')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-03-01', '2022-03-31')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_marzec')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-04-01', '2022-04-30')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_kwiecien')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-05-01', '2022-05-31')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_maj')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-06-01', '2022-06-30')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_czerwiec')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-07-01', '2022-07-31')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_lipiec')

    scrapper_profiles = ScrapperProfiles(profiles, '2022-08-01', '2022-08-31')
    scrapped_tweets = scrapper_profiles.start_scrapping_tweets_date_author_content()
    scrapped_tweets_df = pd.DataFrame(scrapped_tweets, columns=['Date', 'User', 'Tweet'])
    scrapped_tweets_df.to_excel(f'{path}/raporty_autor_content/profiles_content_and_author_sierpien')


def main_scrapper_profiles_about():
    print("I")
    scrapper_profiles_about = ScrapperProfiles(profiles, '2020-11-01', '2020-11-30')
    scrapped_tags = scrapper_profiles_about.start_scrapping_tweets_about_tag('$MATIC')
    scrapper_profiles_raport = Raport('Listopad', scrapped_tags,
                                      f'{path}/scrapper_profiles_about/raport_listopad_MATIC.xlsx')
    scrapper_profiles_raport.create_raport()
    
    print("II")
    scrapper_profiles_about = ScrapperProfiles(profiles, '2020-12-01', '2020-12-31')
    scrapped_tags = scrapper_profiles_about.start_scrapping_tweets_about_tag('$MATIC')
    scrapper_profiles_raport = Raport('Grudzien', scrapped_tags,
                                      f'{path}/scrapper_profiles_about/raport_grudzien_MATIC.xlsx')
    scrapper_profiles_raport.create_raport()
    
    print("III")
    scrapper_profiles_about = ScrapperProfiles(profiles, '2021-01-01', '2021-01-31')
    scrapped_tags = scrapper_profiles_about.start_scrapping_tweets_about_tag('$MATIC')
    scrapper_profiles_raport = Raport('Styczen', scrapped_tags,
                                      f'{path}/scrapper_profiles_about/raport_styczen_MATIC.xlsx')
    scrapper_profiles_raport.create_raport()
    
    print("IV")
    scrapper_profiles_about = ScrapperProfiles(profiles, '2021-02-01', '2021-02-28')
    scrapped_tags = scrapper_profiles_about.start_scrapping_tweets_about_tag('$MATIC')
    scrapper_profiles_raport = Raport('Luty', scrapped_tags,
                                      f'{path}/scrapper_profiles_about/raport_luty_MATIC.xlsx')
    scrapper_profiles_raport.create_raport()
    
    print("V")
    scrapper_profiles_about = ScrapperProfiles(profiles, '2021-03-01', '2021-03-31')
    scrapped_tags = scrapper_profiles_about.start_scrapping_tweets_about_tag('$MATIC')
    scrapper_profiles_raport = Raport('Marzec', scrapped_tags,
                                      f'{path}/scrapper_profiles_about/raport_marzec_MATIC.xlsx')
    scrapper_profiles_raport.create_raport()
    
    print("VI")
    scrapper_profiles_about = ScrapperProfiles(profiles, '2021-11-01', '2021-11-30')
    scrapped_tags = scrapper_profiles_about.start_scrapping_tweets_about_tag('$MATIC')
    scrapper_profiles_raport = Raport('Listopad', scrapped_tags,
                                      f'{path}/scrapper_profiles_about/raport_listopad_MATIC.xlsx')
    scrapper_profiles_raport.create_raport()
