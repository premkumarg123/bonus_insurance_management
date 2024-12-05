import streamlit as st
import psycopg2
import pandas as pd

# Database connection function
def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="753951",  # Replace with your PostgreSQL password
        database="insurance_management"
    )

# Query database
def run_query(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    col_names = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return pd.DataFrame(rows, columns=col_names)

# Streamlit app
st.title("Insurance Management System")
st.sidebar.title("Navigation")

# Navigation options
menu = st.sidebar.radio("Go to", ["Dashboard", "Customers", "Policies", "Claims", "Payments", "Search"])

# Dashboard
if menu == "Dashboard":
    st.header("System Overview")
    try:
        # Metrics
        total_users = run_query("SELECT COUNT(*) AS total FROM users;").iloc[0, 0]
        total_customers = run_query("SELECT COUNT(*) AS total FROM customers;").iloc[0, 0]
        active_policies = run_query("SELECT COUNT(*) AS total FROM insurance;").iloc[0, 0]
        pending_claims = run_query("SELECT COUNT(*) AS total FROM claims WHERE claim_status = 'Pending';").iloc[0, 0]

        # Display metrics
        col1, col2 = st.columns(2)
        col1.metric("Total Users", total_users)
        col2.metric("Total Customers", total_customers)
        col1.metric("Active Policies", active_policies)
        col2.metric("Pending Claims", pending_claims)
    except Exception as e:
        st.error(f"Error: {e}")

# Customers
elif menu == "Customers":
    st.header("Customer Management")
    try:
        customers = run_query("SELECT * FROM customers LIMIT 20;")
        st.dataframe(customers)
    except Exception as e:
        st.error(f"Error: {e}")

# Policies
elif menu == "Policies":
    st.header("Policy Management")
    try:
        policies = run_query("SELECT * FROM insurance LIMIT 20;")
        st.dataframe(policies)
    except Exception as e:
        st.error(f"Error: {e}")

# Claims
elif menu == "Claims":
    st.header("Claims Management")
    try:
        claims = run_query("SELECT * FROM claims WHERE claim_status = 'Pending' LIMIT 20;")
        st.subheader("Pending Claims")
        st.dataframe(claims)

        resolved_claims = run_query("SELECT * FROM claims WHERE claim_status != 'Pending' LIMIT 20;")
        st.subheader("Resolved Claims")
        st.dataframe(resolved_claims)
    except Exception as e:
        st.error(f"Error: {e}")

# Payments
elif menu == "Payments":
    st.header("Payment Management")
    try:
        payments = run_query("SELECT * FROM payments LIMIT 20;")
        st.dataframe(payments)
    except Exception as e:
        st.error(f"Error: {e}")

# Search
elif menu == "Search":
    st.header("Search Database")
    table = st.selectbox("Select Table", ["Users", "Customers", "Vehicles", "Insurance", "Claims", "Payments"])
    query = st.text_area(f"Custom Query for {table}", f"SELECT * FROM {table.lower()} LIMIT 20;")
    if st.button("Execute"):
        try:
            result = run_query(query)
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error: {e}")
