-- Clear existing data
TRUNCATE TABLE Claims CASCADE;
TRUNCATE TABLE Payments CASCADE;
TRUNCATE TABLE Insurance CASCADE;
TRUNCATE TABLE Vehicles CASCADE;
TRUNCATE TABLE Agents CASCADE;
TRUNCATE TABLE Police CASCADE;
TRUNCATE TABLE Customers CASCADE;
TRUNCATE TABLE Users CASCADE;

-- Load updated data
\copy Users FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Users.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Customers FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Customers.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Police FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Police.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Agents FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Agents.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Vehicles FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Vehicles.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Insurance FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Insurance.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Payments FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Payments.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
\copy Claims FROM '/Users/premkumar/Downloads/Milestone2_Vehicle_Insurance/Data files/Claims.csv' WITH (FORMAT csv, HEADER, DELIMITER ',');
