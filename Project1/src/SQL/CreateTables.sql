CREATE DATABASE Shopping_Data;

CREATE TABLE Customers (
    customer_id PRIMARY KEY INT NOT NULL,
    age INT NOT NULL,
    monthly_income FLOAT NOT NULL
);

CREATE TABLE Technology_Usage (
    technology_usage_id PRIMARY KEY SERIAL NOT NULL,
    customer_id INT NOT NULL,
    daily_internet_hours FLOAT NOT NULL,
    smartphone_usage_years FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Social_Behavior (
    social_behavior_id PRIMARY KEY SERIAL NOT NULL,
    customer_id INT NOT NULL,
    social_media_hours FLOAT NOT NULL,
    online_payment_trust_score FLOAT NOT NULL,
    tech_savvy_score FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Shopping_Behavior (
    social_behavior_id PRIMARY KEY SERIAL NOT NULL,
    customer_id INT NOT NULL,
    monthly_online_orders INT NOT NULL,
    monthly_store_visits INT NOT NULL,
    avg_online_spend FLOAT NOT NULL,
    shopping_preference_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (shopping_preference_id) REFERENCES Shopping_Preference(shopping_preference_id)
);

CREATE TABLE Shopping_Preference (
    shopping_preference_id PRIMARY KEY SERIAL NOT NULL,
    preference_name VARCHAR(50) NOT NULL
);

CREATE TABLE Invalid_Entries ( -- entries containing null values or were duplicates
    invalid_entry_id PRIMARY KEY SERIAL NOT NULL,
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
    shopping_preference VARCHAR(10),
)