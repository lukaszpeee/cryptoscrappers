import pandas as pd
from data.dictionaries import profiles
from scrappers.ScrapperProfiles import ScrapperProfiles


class ScrapperProfilesRaport:
    
    def __init__(self, since_date: str, until_date: str, raport_path: str):
        self.since_date = since_date
        self.until_date = until_date
        self.raport_path = raport_path
        
    def create_scrapper_profiles_raport(self):
        scrapper_profiles = ScrapperProfiles(profiles, self.since_date, self.until_date)
        scrapper_profiles.start_scrapping_tweets()
        scrapper_profiles.start_extracting_tags()
        tags = [tag.upper() for tag in scrapper_profiles.extracted_tags]
        df_tags = pd.DataFrame(tags, columns=['Tag'])
        df_counted_tags = df_tags.groupby(['Tag'])['Tag'].count().sort_values(ascending=False)
        df_counted_tags.to_excel(self.raport_path)