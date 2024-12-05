from flask import Flask, render_template, request, flash
import psycopg2
import os  # Required for reading environment variables

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key")  # Use Heroku's environment variable for security

# Database connection
def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "753951"),
        database=os.getenv("DB_NAME", "insurance_management")
    )

# Home Route
@app.route('/')
def home():
    return render_template('base.html')

# User Portal
@app.route('/user', methods=['GET', 'POST'])
def user_portal():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        dl_number = request.form.get('dl_number')
        address = request.form.get('address')
        vehicle_model = request.form.get('vehicle_model')

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Generate a new customer_id
            cursor.execute("SELECT COALESCE(MAX(customer_id), 0) + 1 FROM customers;")
            customer_id = cursor.fetchone()[0]

            # Insert into Customers table
            cursor.execute("""
                INSERT INTO customers (customer_id, customer_name, customer_age, dl_num, customer_address)
                VALUES (%s, %s, %s, %s, %s);
            """, (customer_id, name, age, dl_number, address))

            # Generate a new vehicle_id
            cursor.execute("SELECT COALESCE(MAX(vehicle_id), 0) + 1 FROM vehicles;")
            vehicle_id = cursor.fetchone()[0]

            # Insert into Vehicles table
            cursor.execute("""
                INSERT INTO vehicles (vehicle_id, model, customer_id)
                VALUES (%s, %s, %s);
            """, (vehicle_id, vehicle_model, customer_id))

            conn.commit()
            flash("Insurance profile created successfully!", "success")
        except Exception as e:
            conn.rollback()
            flash(f"Error: {str(e)}", "danger")
        finally:
            conn.close()

    return render_template('user.html')

# Add remaining routes (police, agent, admin, claims, payments) as they are without modification
# as shown in the original code above.

# Run the app
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Heroku dynamically assigns a port
    app.run(host="0.0.0.0", port=port, debug=True)
