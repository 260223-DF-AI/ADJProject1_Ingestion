"""The main parser for our project."""

import pandas as pd

import logging
from datetime import datetime

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('message.log')
fomatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

logger.setLevel(logging.INFO)

console_handler.setFormatter(fomatter)
file_handler.setFormatter(fomatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def read_file_subset(filepath, subset=[]):
    """reads the given CSV and returns a dataframe

        Input: 
            - Filepath : path to the file
            - subset : LIST of column names that you want to keep (default is all)
        Output:
            - Dataframe with your csv read, data is NOT cleaned

    """

    # read the file
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Read csv file {filepath} into pandas dataframe")
    except pd.errors.EmptyDataError as e:
        logger.warning(f"File is empty. Error message: {e}")
        return None
    except pd.errors.ParserError as e:
        logger.warning(f"Error parsing the CSV file. Error message: {e}")
        raise RuntimeError("Something went wrong with the parsing, try again e:",e)
    except FileNotFoundError as e:
        logger.warning(f"File not found. Error message: {e}")
        raise FileNotFoundError("Filepath wrong e:",e)
    except Exception as e:
        logger.error(f"An unexpected error occurred. Error message: {e}")
        exit(-1) # quit now, we need to fix this

    # extract subset of data we want to work with if any
    if not subset:
        return df
    else:
        return df[subset]




# this is something we can't fully automate and would need code changes, this is because
# it takes input from a human to decide what types we want to store everything in the DB
def clean_data(df):
    """Cleans the given Dataframe
    
    -Converts numerical entries to Int/Float
    - decide if there are too many NaN entries and if we need to drop a col, or do we fill
    - removes duplicate rows, strip whitespace and standardize text
    
    """
    # Our subset in THIS dataset
    # age (int) ,monthly_income (float ),daily_internet_hours(float),smartphone_usage_years(float),social_media_hours(float),
    # online_payment_trust_score(float),tech_savvy_score(float),monthly_online_orders(int),monthly_store_visits(int),
    # avg_online_spend(float),shopping_preference(string)
    #

    # DROP things here

    rejected_rows = df[df.duplicated(keep='first') | df.isnull().any(axis=1)]

    na_rows = df[df.isnull().any(axis=1)]
    logger.info(f"na rows: {na_rows}")
    df.dropna(inplace=True) # drop rows with any NaN values

    dupe_rows = df[df.duplicated(keep='first')]
    logger.info(f"dupe rows: {dupe_rows}")
    df.drop_duplicates(inplace=True) # drop duplicate rows


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
    df["shopping_preference"] = df["shopping_preference"].apply(lambda x : x.strip().lower())

    # type conversions
    rejected_rows["age"] = rejected_rows["age"].astype(int)
    rejected_rows["monthly_income"] = rejected_rows["monthly_income"].astype(float)
    rejected_rows["daily_internet_hours"] = rejected_rows["daily_internet_hours"].astype(float)
    rejected_rows["smartphone_usage_years"] = rejected_rows["smartphone_usage_years"].astype(float)
    rejected_rows["social_media_hours"] = rejected_rows["social_media_hours"].astype(float)
    rejected_rows["online_payment_trust_score"] = rejected_rows["online_payment_trust_score"].astype(float)
    rejected_rows["tech_savvy_score"] = rejected_rows["tech_savvy_score"].astype(float)
    rejected_rows["monthly_online_orders"] = rejected_rows["monthly_online_orders"].astype(int)
    rejected_rows["monthly_store_visits"] = rejected_rows["monthly_store_visits"].astype(int)
    rejected_rows["avg_online_spend"] = rejected_rows["avg_online_spend"].astype(float)
    rejected_rows["shopping_preference"] = rejected_rows["shopping_preference"].astype(str)
    
    # string standardizing
    rejected_rows["shopping_preference"] = rejected_rows["shopping_preference"].apply(lambda x : x.strip().lower())

    return (df, rejected_rows)



def add_id_feature(df):
    "Adds a unique id to each row"
    #print(df.shape)
    arr = list(range(df.shape[0]))
    #print(arr)
    df["id"] = arr
    
    return df


# preprocessing that's specific to our dataset, this would need to be changed
def preprocessing(df):
    # preprocessing all the tables
    df = add_id_feature(df)
    shopping_mapper = {"store":0, "online":1}
    # change to our id
    df["shopping_prefence"] = df["shopping_preference"].apply(lambda x : shopping_mapper[x])

    customers_table = df[["id","age","monthly_income"]]
    technology_usage_table = df[["id","daily_internet_hours","smartphone_usage_years"]]
    social_behavior_table = df[["id","social_media_hours", "online_payment_trust_score", "tech_savvy_score"]]
    shopping_behavior_table = df[["id","monthly_online_orders", "monthly_store_vists", "average_online_spending","shopping_prefernce"]]
    shopping_preference_table = df[["shopping_prefernce"]]

    # DO STUFF LATER