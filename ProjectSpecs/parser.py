"""The main parser for our project."""

import pandas as pd



def read_file_subset(filepath, subset=[]):
    """reads the given CSV and returns a dataframe

        Input: 
            - Filepath : path to the file
            - subset : LIST of column names that you want to keep (default is all)
        Output:
            - Dataframe with your csv read, data is NOT cleaned
    """

    # read the file
    df = pd.read_csv(filepath)

    # extract subset of data we want to work with if any
    if not subset:
        return df
    else:
        return df[subset]
    

def clean_data(df):
    """Cleans the given Dataframe
    
    -Converts numerical entries to Int/Float
    - TODO decide if there are too many NaN entries and if we need to drop a col, or do we fill
    - removes duplicate rows, strip whitespace and standardize text
    
    """
    # Our subset in THIS dataset
    # age (int) ,monthly_income (float ),daily_internet_hours(float),smartphone_usage_years(float),social_media_hours(float),
    # online_payment_trust_score(float),tech_savvy_score(float),monthly_online_orders(int),monthly_store_visits(int),
    # avg_online_spend(float),shopping_preference(string)
    #

    # TODO decide whether to drop anything here



    # type conversions
    df["age"] = df["age"].astype(int)
    df["monthly_income"] = df["monthly_income"].astype(float)
    df["daily_internet_hours"] = df["daily_internet_hours"].astype(float)
    df["smartphone_usage_years"] = df["smartphone_usage_years"].astype(float)
    df["social_media_hours"] = df["social_media_hours"].astype(float)
    df["online_payment_trust_score"] = df["online_payment_trust_score"].astype(float)
    df["tech_savvy_score"] = df["tech_savvy_score"].astype(float)
    df["monthly_online_orders"] = df["monthly_online_orders"].astype(int)
    df["monthly_store_visits"] = df["monthly_store_visits"].astype(int)
    df["avg_online_spend"] = df["avg_online_spend"].astype(float)
    df["shopping_preference"] = df["shopping_preference"].astype(str)
    
    # string standardizing
    df["shopping_preference"] = df["shopping_preference"].applymap(lambda x : x.strip().lower())

    return df