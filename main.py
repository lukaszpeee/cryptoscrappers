import time

from scrappers.ScrapperProfiles.usecase import main_scrapper_profiles_for_month, \
    main_scrapper_tweets_date_author_content_for_month


if __name__ == "__main__":
    path = 'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/'
    start_time = time.time()
    # main_scrapper_profiles_for_month(path)
    main_scrapper_tweets_date_author_content_for_month(path)
    print(f"{(time.time() - start_time)/60} mins")
