-- creating database
CREATE DATABASE IF NOT EXISTS Shopping_Data;

-- creating Customers table
-- PK: customer_id
DROP IF EXISTS Customers
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    age INT NOT NULL,
    monthly_income FLOAT NOT NULL
);

-- creating Technology_Usage table
-- PK: technology_usage_id
-- FK: customer_id from Customers table
DROP IF EXISTS Technology_Usage
CREATE TABLE Technology_Usage (
    technology_usage_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    daily_internet_hours FLOAT NOT NULL,
    smartphone_usage_years FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- creating Social_Behavior table
-- PK: social_behavior_id
-- FK: customer_id from Customers table
DROP IF EXISTS Social_Behavior
CREATE TABLE Social_Behavior (
    social_behavior_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    social_media_hours FLOAT NOT NULL,
    online_payment_trust_score FLOAT NOT NULL,
    tech_savvy_score FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- creating Shopping_Preference table
-- PK: shopping_preference_id
DROP IF EXISTS Shopping_Preference
CREATE TABLE Shopping_Preference (
    shopping_preference_id SERIAL PRIMARY KEY,
    preference_name VARCHAR(50) NOT NULL
);

-- creating Shopping_Behavior table
-- PK: shopping_behavior_id
-- FK: customer_id from Customers table
-- FK: shopping_preference_id from Shopping_Preference table
DROP IF EXISTS Shopping_Behavior
CREATE TABLE Shopping_Behavior (
    shopping_behavior_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    monthly_online_orders INT NOT NULL,
    monthly_store_visits INT NOT NULL,
    avg_online_spend FLOAT NOT NULL,
    shopping_preference_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (shopping_preference_id) REFERENCES Shopping_Preference(shopping_preference_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- creating Invalid_Entries table
-- PK: invalid_entry_id
DROP IF NOT EXISTS Invalid_Entries
CREATE TABLE Invalid_Entries ( -- entries containing null values or were duplicates
    invalid_entry_id SERIAL PRIMARY KEY,
    age INT,
    monthly_income FLOAT,
    daily_internet_hours FLOAT,
    smartphone_usage_years FLOAT,
    social_media_hours FLOAT,
    online_payment_trust_score FLOAT,
    tech_savvy_score FLOAT,
    monthly_online_orders INT,
    monthly_store_visits INT,
    avg_online_spend FLOAT,
    shopping_preference VARCHAR(10)
)