import time

from scrappers.ScrapperProfiles.main import main_scrapper_profiles_about

if __name__ == "__main__":
    path = 'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile'
    start_time = time.time()
    # main_scrapper_profiles()
    # main_scrapper_tags()
    main_scrapper_profiles_about()
    print(f"{(time.time() - start_time)/60} mins")
