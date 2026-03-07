"""File to test parser.py functionality"""
import pytest
from src.parser import clean_data
import pandas as pd

def test_parser(): # TODO implement this + whatever you think might be useful to test on parser
    """Test parser.py functionality"""
    assert False, "not implemented"



def test_clean_data():
    """Test clean_data function in parser.py"""
    
    # get sample data from test_subset.csv
    sample_data = pd.read_csv('tests/test_subset.csv')
    print("Sample data before cleaning:")
    print(sample_data)
    # expected output after cleaning the data
    # expected behavior changes:
    #   - rows 6 and 7 are duplicates, so drop them
    #   - Row 8 has nan values so it should be dropped
    #   - text for "Store" and " Hybrid" should be standardized to "store" and "hybrid" (strip whitespace and lowecase it all)
    # these are expected rows and typings     
    # age (int) ,monthly_income (float ),daily_internet_hours(float),smartphone_usage_years(float),social_media_hours(float),
    # online_payment_trust_score(float),tech_savvy_score(float),monthly_online_orders(int),monthly_store_visits(int),
    # avg_online_spend(float),shopping_preference(string)
    expected_output = pd.DataFrame({
        'age': [56, 69, 46, 32, 60],
        'monthly_income': [221111.0, 96029.0, 19055.0, 53170.0, 244016.0],
        'daily_internet_hours': [6.5, 8.2, 6.4, 6.4, 6.0],
        'smartphone_usage_years': [12.0, 13.0, 4.0, 11.0, 5.0],
        'social_media_hours': [0.7, 2.7, 2.1, 0.7, 0.7],
        'online_payment_trust_score': [1.0, 6.0, 10.0, 2.0, 2.0],
        'tech_savvy_score': [6.0, 9.0, 8.0, 10.0, 5.0],
        'monthly_online_orders': [16, 14, 2, 20, 18],
        'monthly_store_visits': [16, 1, 0, 3, 16],
        'avg_online_spend': [28551.0, 124056.0, 81939.0, 35901.0, 131971.0],
        'shopping_preference': ['store', 'hybrid', 'store', 'store', 'store']
    })

    print(expected_output)
    # clean the data using the function
    cleaned_data = clean_data(sample_data)
    print("Cleaned data:")
    print(cleaned_data)
    # assert that the cleaned data matches the expected output
    test = cleaned_data.compare(expected_output)
    assert test.empty, f"Cleaned data does not match expected output diff:{cleaned_data.compare(test)}"


