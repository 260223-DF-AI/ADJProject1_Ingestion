CREATE TABLE Customers (
    customer_id INT PRIMARY KEY NOT NULL,
    age INT NOT NULL,
    monthly_income FLOAT NOT NULL
);

CREATE TABLE Technology_Usage (
    customer_id INT NOT NULL,
    daily_internet_hours FLOAT NOT NULL,
    smartphone_usage_years FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Social_Behavior (
    customer_id INT NOT NULL,
    social_media_hours FLOAT NOT NULL,
    online_payment_trust_score FLOAT NOT NULL,
    tech_savvy_score FLOAT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Shopping_Behavior (
    customer_id INT NOT NULL,
    monthly_online_orders INT NOT NULL,
    monthly_store_visits INT NOT NULL,
    avg_online_spend FLOAT NOT NULL,
    shopping_preference_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (shopping_preference_id) REFERENCES Shopping_Preference(shopping_preference_id)
);

CREATE TABLE Shopping_Preference (
    shopping_preference_id INT PRIMARY KEY NOT NULL,
    preference_name VARCHAR(50) NOT NULL
);
