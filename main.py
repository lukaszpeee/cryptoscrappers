import time
from ScrapperProfiles import ScrapperProfiles
from ScrapperTagsCrypto import ScrapperTagsCrypto
from dictionaries import profiles, tagscrypto


def main():
    scrapper_profiles = ScrapperProfiles(profiles, '2022-08-01', '2022-08-07')
    scrapper_profiles.start_scrapping()
    
    # scrapper_tags_crypto= ScrapperTagsCrypto(tagscrypto, '2022-08-01', '2022-08-02')
    # scrapper_tags_crypto.start_scrapping()

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))