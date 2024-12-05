This project focuses on designing and implementing a relational database system to optimize data management for the vehicle insurance industry. By addressing challenges like scalability, data integrity, redundancy elimination, and query performance, the system improves operations and enhances decision-making for insurance companies, agents, and customers.

Data Source
The database schema and sample data were designed using:

Generated Data: Unique identifiers and records were created using Python’s Faker library for a realistic dataset.
Partial Sources: A subset of insurance-related datasets was used from platforms like Kaggle.
Tables and Schema
The database comprises the following key tables:

Users: Stores user information such as roles and credentials.
Customers: Tracks customer profiles, personal details, and linked user IDs.
Vehicles: Records information about customer vehicles, safety features, and fuel types.
Insurance: Manages policies, their status, and associations with vehicles and customers.
Claims: Tracks claims, including amounts, dates, and resolution details.
Payments: Records payments for policies, payment dates, methods, and statuses.
Agents: Stores insurance agent details and their associated user IDs.
Police: Maintains police records linked to incidents and user IDs.
Features and Functionalities
Data Normalization: Ensures tables conform to BCNF principles, improving data consistency and reducing redundancy.
SQL Queries: Demonstrates advanced operations such as joins, aggregations, filtering, and subqueries.
Indexing: Applied on key columns (e.g., customer_id, policy_id) to enhance query performance for large datasets.
Streamlit Integration: Provides a dynamic web interface for querying and visualizing data interactively.
Database Integration and Loading
Tables Creation: Schema designed using create.sql.
Data Loading: Data imported into PostgreSQL through load.sql after initial processing with a consolidated mega table.
Query Demonstrations
To showcase the database's capabilities, several queries were executed and optimized, including:

Identifying high-value claims and pending resolutions.
Analyzing vehicle insurance status and underperforming policies.
Calculating total payments for specific agents or policies.
Visualizing claims trends based on customer demographics.
Tools and Technologies
Database Management System: PostgreSQL
Programming Language: Python
Libraries: Faker, Pandas, Plotly, Streamlit
ER Diagram Tool: dbdiagram.io
Results and Reports
The executed queries provided actionable insights, including:

Trends in claims resolution time.
Analysis of policy performance by region or agent.
Identification of high-cost insurance cases and their impact. All findings are documented in the final report, demonstrating the system's effectiveness.
Conclusion
This project underscores the importance of a well-structured database for managing large-scale data in the vehicle insurance industry. By replacing inefficient tools and processes, the system ensures enhanced scalability, better decision-making, and improved operational efficiency for all stakeholders. The addition of a user-friendly Streamlit interface further simplifies interaction with the database, making the solution highly accessible and practical.