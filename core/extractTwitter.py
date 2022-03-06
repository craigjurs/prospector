# Author:           Craig JURS
# Python Version:   3.6
# project:          
# Copyright:        Michelin North America, 2020
# =============================================================================
"""extract text from twitter using a list of search terms"""
# =============================================================================
# Imports
from twitterscraper import query_tweets
import pandas as pd
# =============================================================================

class ExtractFromTwitter():
    def __init__(self, begin_date, end_date, limit=1000, language='english'):
        self.search_terms = list()

        self.begin_date = begin_date
        self.end_date = end_date
        self.limit = limit
        self.language = language

    def company_tweets_to_dictionary(self, company_list=["bridgstone", "cooper tire", "firestone", "michelin", "pirelli", "goodyear", "dunlop", "bfgoodrich"]):
        self.search_terms_list = [company + ' AND ' + self.search_terms for company in company_list]
        self.company_tweets = dict()
        for search in self.search_terms_list:
            tweets = query_tweets(search,
                                  begindate=self.begin_date,
                                  enddate=self.end_date,
                                  lang=self.language)
            try:
                temp_df = pd.DataFrame(t.__dict__ for t in tweets)
                temp_df.sort_values(by='timestamp', ascending=False, inplace=True)
                self.company_tweets[search.split()[0]] = temp_df
            except:
                print('search of terms: ' + search + ' did not show any results')
                pass

    def compile_company_tweet_dictionary_to_pandas(self, sort_by_date = True):
        df_list = []
        for key, df in self.company_tweets.items():
            if key:
                company = [key] * len(df)
                temp_df = pd.concat([pd.DataFrame({'company': company}),
                                     self.company_tweets[key].reset_index(drop=True)], axis=1)
                df_list.append(temp_df)
        self.df_tweets = pd.concat(df_list)
        if sort_by_date:
            self.df_tweets.sort_values(by='timestamp', ascending=False, inplace=True)

