CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(255),
    role VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    customer_name VARCHAR(100),
    customer_address VARCHAR(200),
    customer_age INTEGER,
    dl_num CHAR(5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Vehicles (
    vehicle_id INTEGER PRIMARY KEY,
    model VARCHAR(50),
    vehicle_age NUMERIC(5, 2),
    segment VARCHAR(20),
    fuel_type VARCHAR(10),
    airbags INTEGER,
    ncap_rating INTEGER,
    is_parking_camera VARCHAR(3),
    is_speed_alert VARCHAR(3),
    is_brake_assist VARCHAR(3),
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Insurance (
    policy_id VARCHAR(50) PRIMARY KEY, -- Increased VARCHAR length for larger IDs
    subscription_length NUMERIC(5, 2),
    claim_status VARCHAR(30),
    vehicle_id INTEGER,
    customer_id INTEGER,
    FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Claims (
    claim_id INTEGER PRIMARY KEY,
    policy_id VARCHAR(50),
    customer_id INTEGER,
    claim_date DATE NOT NULL,
    claim_amount NUMERIC(15, 2) NOT NULL, -- Increased precision to accommodate large values
    claim_status VARCHAR(20) NOT NULL,
    resolution_date DATE,
    FOREIGN KEY (policy_id) REFERENCES Insurance(policy_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Agents (
    agent_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    agent_name VARCHAR(100) NOT NULL,
    contact_number VARCHAR(15),
    email VARCHAR(100) NOT NULL UNIQUE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Payments (
    payment_id INTEGER PRIMARY KEY,
    policy_id VARCHAR(50),
    customer_id INTEGER,
    payment_date DATE NOT NULL,
    amount BIGINT NOT NULL, -- Changed from INTEGER to BIGINT for large values
    payment_method VARCHAR(50),
    payment_status VARCHAR(20) NOT NULL,
    FOREIGN KEY (policy_id) REFERENCES Insurance(policy_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Police (
    police_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    police_name TEXT NOT NULL,
    police_station TEXT NOT NULL,
    police_contact TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
