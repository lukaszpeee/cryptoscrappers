import time
from data.dictionaries import profiles, tagscrypto, tagscrypto_tests, profiles_tests
import pandas as pd

from scrappers.ScrapperProfile import ScrapperProfile
from scrappers.ScrapperProfiles import ScrapperProfiles
from scrappers.ScrapperTagsCrypto import ScrapperTagsCrypto
from scrappers.ScrapperTagCrypto import ScrapperTagCrypto
from raports.Raport import Raport
from raports.MergedRaport import MergedRaport
from raports.VerificationMergedRaport import (VeriticationAllMonths,
                                              VeriticationFirstAndLast,
                                              VeriticationFirstThreeMonths,
                                              VeriticationLastFreeMonths)
from data.raports import raport_01, raport_02, raport_03, raport_04, raport_05, raport_06, raport_07, raport_08


def main(): 
    # scrapper_profiles = ScrapperProfiles(profiles_tests, '2022-08-01', '2022-08-31')
    # scrapper_profiles.start_scrapping_tweets()
    # scrapper_profiles.start_extracting_tags()
    # scrapper_raport = ScrapperProfilesRaport(
    #     'Sierpien',
    #     scrapper_profiles.extracted_tags,
    #     'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/raport_test.xlsx')
    # scrapper_raport.create_scrapper_profiles_raport()
    
    # raports = [raport_01, raport_02, raport_03, raport_04, raport_05, raport_06, raport_07, raport_08]
    # new_raport = MergedRaport(raports,
    #     'C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/completed_raport.xlsx')
    
    # merged_raports = new_raport.merge_raports('Tag')
    
    # ver_fal = VeriticationFirstAndLast(merged_raports)
    # ver_fal = ver_fal.make_verivication()
    
    # ver_ftm = VeriticationFirstThreeMonths(ver_fal)
    # ver_ftm = ver_ftm.make_verivication()
    
    # ver_ltm = VeriticationLastFreeMonths(ver_ftm)
    # ver_ltm = ver_ltm.make_verivication()
    
    # ver_all = VeriticationAllMonths(ver_ltm)
    # ver_all = ver_all.make_verivication()
    # ver_all.to_excel('C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/verification_merged_raport.xlsx')
    scrapper_profiles_about = ScrapperProfiles(profiles, '2022-01-01', '2022-08-31')
    scrapper_profiles_about = scrapper_profiles_about.start_scrapping_tweets_about('EVMOS')
    scrapper_profiles_about.to_excel('C:/Users/rogal/Desktop/Kryptowaluty/raporty_profile/evmos_raport_styczen_sierpien.xlsx')


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"{(time.time() - start_time)/60} mins")
