"""File to test parser.py functionality"""
import pytest
from src.parser import clean_data, read_file_subset
import pandas as pd

class TestParserFunctionality:
    """Test all of the parser's edgecases"""

    def test_file_not_found(self): # TODO implement this + whatever you think might be useful to test on parser
        """Test file not found when parsing"""
        with pytest.raises(FileNotFoundError):
            read_file_subset("NotAValidFile", [])

    def test_empty_file(self, tmp_path):    # tmp_path is a built in pytest feature that creates a temporary file on disk that gets cleaned up automatically after test is run
        """Test file is empty — function catches EmptyDataError and returns None"""
        empty_file = tmp_path / "empty_file.csv"
        empty_file.write_text("")
        result = read_file_subset(str(empty_file), [])
        assert result is None

    def test_parsing_error(self, tmp_path):
        """Test that a malformed/corrupt file raises a RuntimeError (wrapped by the function)"""
        bad_file = tmp_path / "malformed.csv"
        bad_file.write_text("col1,col2\n1,2,3\n4,5,6,7")  # inconsistent columns
        with pytest.raises(RuntimeError):
            read_file_subset(str(bad_file), [])

    def test_reading_file(self):
        """Test reading in a file with a given subset"""
        # ARRANGE
        # expected output when reading the data:
        # 11 columns with 7 rows
        # 2 rows have only 6 non NULL values
        expected_output = pd.DataFrame({
        'age': [56, 69, 46, 32, 60, 60, 60],
        'monthly_income': [221111.0, 96029.0, 19055.0, 53170.0, 244016.0, 244016.0, 244016.0],
        'daily_internet_hours': [6.5, 8.2, 6.4, 6.4, 6.0, 6.0, 6.0],
        'smartphone_usage_years': [12.0, 13.0, 4.0, 11.0, 5.0, 5.0, 5.0],
        'social_media_hours': [0.7, 2.7, 2.1, 0.7, 0.7, 0.7, 0.7],
        'online_payment_trust_score': [1.0, 6.0, 10.0, 2.0, 2.0, 2.0, 2.0],
        'tech_savvy_score': [6.0, 9.0, 8.0, 10.0, 5.0, 5.0, None],
        'monthly_online_orders': [16, 14, 2, 20, 18, 18, 18],
        'monthly_store_visits': [16, 1, 0, 3, 16, 16, 16],
        'avg_online_spend': [28551.0, 124056.0, 81939.0, 35901.0, 131971.0, 131971.0, None],
        'shopping_preference': ['Store', 'Hybrid', 'Store', 'Store', 'Store', 'Store', 'Store']
        })
        # ACT
        # get data frame from reading in the file
        subset = [
            'age', 'monthly_income', 'daily_internet_hours', 'smartphone_usage_years', 'social_media_hours', 'online_payment_trust_score',
            'tech_savvy_score', 'monthly_online_orders', 'monthly_store_visits', 'avg_online_spend', 'shopping_preference'
        ]
        df = read_file_subset('tests/test_subset.csv', subset)
        test = df.compare(expected_output)
        # assert 
        assert test.empty, f"Cleaned data does not match expected output diff:{df.compare(test)}"
        


    def test_read_file_no_subset_returns_all_columns(self, tmp_path):
        """When subset is empty (default), all columns from the CSV are returned"""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("col1,col2,col3\n1,2,3\n4,5,6")
        df = read_file_subset(str(csv_file))
        assert list(df.columns) == ["col1", "col2", "col3"]
        assert len(df) == 2

    def test_read_file_with_subset_returns_only_requested_columns(self, tmp_path):
        """When a subset list is provided, only those columns are returned"""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("col1,col2,col3\n1,2,3\n4,5,6")
        df = read_file_subset(str(csv_file), ["col1", "col3"])
        assert list(df.columns) == ["col1", "col3"]
        assert "col2" not in df.columns

    def test_read_file_subset_preserves_row_count(self, tmp_path):
        """Row count is preserved when selecting a subset of columns"""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("a,b,c\n1,2,3\n4,5,6\n7,8,9")
        df = read_file_subset(str(csv_file), ["a", "b"])
        assert len(df) == 3

    def test_read_file_invalid_column_raises_key_error(self, tmp_path):
        """Requesting a column that does not exist raises a KeyError"""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("col1,col2\n1,2")
        with pytest.raises(KeyError):
            read_file_subset(str(csv_file), ["col1", "nonexistent_col"])

    def test_read_file_returns_dataframe(self, tmp_path):
        """Return type is always a pandas DataFrame"""
        csv_file = tmp_path / "data.csv"
        csv_file.write_text("x,y\n10,20")
        result = read_file_subset(str(csv_file))
        assert isinstance(result, pd.DataFrame)


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
