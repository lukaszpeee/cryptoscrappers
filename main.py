import time
from scrappers.ScrapperProfile import ScrapperProfile
from scrappers.ScrapperProfiles import ScrapperProfiles
from scrappers.ScrapperTagsCrypto import ScrapperTagsCrypto
from scrappers.ScrapperTagCrypto import ScrapperTagCrypto
from data.dictionaries import profiles, tagscrypto


def main():
    # scrapper_profile = ScrapperProfile('elonmusk', '2022-08-01', '2022-08-07')
    # scrapper_profile.start_scrapping()
    
    scrapper_profiles = ScrapperProfiles(profiles, '2022-08-01', '2022-08-29')
    scrapper_profiles.start_scrapping()
    
    # scrapper_tags_crypto= ScrapperTagsCrypto(tagscrypto, '2022-08-01', '2022-08-02')
    # scrapper_tags_crypto.start_scrapping()
    
    # scrapper_tag_crypto= ScrapperTagCrypto('eth', '2022-08-01', '2022-08-02')
    # scrapper_tag_crypto.start_scrapping()


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"{(time.time() - start_time)/60} mins")
