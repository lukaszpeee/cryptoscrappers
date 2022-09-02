import time
from raports.ScrapperProfilesRaport import ScrapperProfilesRaport
from scrappers.ScrapperProfile import ScrapperProfile
from scrappers.ScrapperProfiles import ScrapperProfiles
from scrappers.ScrapperTagsCrypto import ScrapperTagsCrypto
from scrappers.ScrapperTagCrypto import ScrapperTagCrypto
from data.dictionaries import profiles, tagscrypto, tagscrypto_tests, profiles_tests
import pandas as pd


def main():
    scrapper_profiles_raport = ScrapperProfilesRaport(
        '2022-08-01', '2022-08-31', 'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/raport_sierpien.xlsx')
    scrapper_profiles_raport.create_scrapper_profiles_raport()
    
    # scrapper_profile = ScrapperProfile('elonmusk', '2022-08-01', '2022-08-07')
    # scrapper_profile.start_scrapping()
    
    # scrapper_tags_crypto= ScrapperTagsCrypto(tagscrypto, '2022-08-01', '2022-08-02')
    # scrapper_tags_crypto.start_scrapping()
    
    # scrapper_tag_crypto= ScrapperTagCrypto('eth', '2022-08-01', '2022-08-02')
    # scrapper_tag_crypto.start_scrapping()


if __name__ == "__main__":
    raport_path = 'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/raport_sierpien.xlsx'
    start_time = time.time()
    main()
    print(f"{(time.time() - start_time)/60} mins")
