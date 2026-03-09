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

            TODO : change all them prints to logs when we get that set up
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

    na_rows = df[df.isnull().any(axis=1)]
    logger.info(f"na rows: {na_rows}")
    df.dropna(inplace=True) # drop rows with any NaN values

    dupe_rows = df[df.duplicated(keep=False)]
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

    return df



def add_id_feature(df):
    "Adds a unique id to each row"
    #print(df.shape)
    arr = list(range(df.shape[0]))
    #print(arr)
    df["id"] = arr
    
    return df