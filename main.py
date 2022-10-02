import time

from scrappers.ScrapperProfiles.usecase import main_scrapper_profiles_content_and_author, \
    main_scrapper_profiles_for_month

if __name__ == "__main__":
    path = 'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile'
    start_time = time.time()
    # main_scrapper_profiles()
    # main_scrapper_tags()
    # main_scrapper_profiles_about()
    main_scrapper_profiles_for_month(path)
    # main_scrapper_profiles_content_and_author(path)
    print(f"{(time.time() - start_time)/60} mins")
