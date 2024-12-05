from flask import Flask, render_template, request, flash
import psycopg2

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a secure secret key

# Database connection
def get_connection():
    return psycopg2.connect(
        host="localhost",  # Replace with the ngrok host
        port="5432",           # Replace with the ngrok port
        user="postgres",        # Your PostgreSQL username
        password="753951",  # Your PostgreSQL password
        database="insurance_management"
    )

# Home Route
@app.route('/')
def home():
    return render_template('base.html')

# User Portal
@app.route('/user', methods=['GET', 'POST'])
def user_portal():
    if request.method == 'POST':
        # Capture form input
        name = request.form.get('name')
        age = request.form.get('age')
        dl_number = request.form.get('dl_number')
        address = request.form.get('address')
        vehicle_model = request.form.get('vehicle_model')

        print(f"Received: Name={name}, Age={age}, DL={dl_number}, Address={address}, Vehicle={vehicle_model}")

        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Generate a new customer_id
            cursor.execute("SELECT COALESCE(MAX(customer_id), 0) + 1 FROM customers;")
            customer_id = cursor.fetchone()[0]
            print(f"Generated Customer ID: {customer_id}")

            # Insert into Customers table
            cursor.execute("""
                INSERT INTO customers (customer_id, customer_name, customer_age, dl_num, customer_address)
                VALUES (%s, %s, %s, %s, %s);
            """, (customer_id, name, age, dl_number, address))
            print(f"Inserted into Customers: {name}, ID={customer_id}")

            # Generate a new vehicle_id
            cursor.execute("SELECT COALESCE(MAX(vehicle_id), 0) + 1 FROM vehicles;")
            vehicle_id = cursor.fetchone()[0]
            print(f"Generated Vehicle ID: {vehicle_id}")

            # Insert into Vehicles table
            cursor.execute("""
                INSERT INTO vehicles (vehicle_id, model, customer_id)
                VALUES (%s, %s, %s);
            """, (vehicle_id, vehicle_model, customer_id))
            print(f"Inserted into Vehicles: {vehicle_model}, Vehicle ID={vehicle_id}")

            conn.commit()
            flash("Insurance profile created successfully!", "success")
        except Exception as e:
            conn.rollback()  # Rollback in case of an error
            flash(f"Error: {str(e)}", "danger")
        finally:
            conn.close()

    return render_template('user.html')


# Police Portal
@app.route('/police', methods=['GET', 'POST'])
def police_portal():
    details = None  # Initialize details as None
    message = None  # Initialize message as None
    if request.method == 'POST':
        search_term = request.form.get('search')  # Get the search term from the form
        print(f"Search Term: {search_term}")  # Debugging
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT c.customer_name, c.customer_age, c.customer_address, v.model
                FROM customers c
                JOIN vehicles v ON c.customer_id = v.customer_id
                WHERE c.dl_num = %s OR v.vehicle_id::TEXT = %s;
            """, (search_term, search_term))
            details = cursor.fetchone()  # Fetch a single result
            if not details:
                message = "No records found for the given Vehicle ID or DL Number."
            conn.close()
        except Exception as e:
            message = f"Error: {str(e)}"
    return render_template('police.html', details=details, message=message)



# Agent Portal
@app.route('/agent', methods=['GET', 'POST'])
def agent_portal():
    policies = None
    claims = None
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Fetch customer policies
            cursor.execute("""
                SELECT i.policy_id, i.subscription_length, i.claim_status, v.model
                FROM insurance i
                JOIN vehicles v ON i.vehicle_id = v.vehicle_id
                WHERE i.customer_id = %s;
            """, (customer_id,))
            policies = cursor.fetchall()

            # Fetch customer claims
            cursor.execute("""
                SELECT claim_id, claim_date, claim_amount, claim_status
                FROM claims
                WHERE customer_id = %s;
            """, (customer_id,))
            claims = cursor.fetchall()

            conn.close()
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
    return render_template('agent.html', policies=policies, claims=claims)


# Admin Portal
@app.route('/admin')
def admin_portal():
    stats = {}
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Fetch statistics
        cursor.execute("SELECT COUNT(*) FROM customers;")
        stats['total_customers'] = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM insurance;")
        stats['total_policies'] = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM claims;")
        stats['total_claims'] = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM payments;")
        stats['total_payments'] = cursor.fetchone()[0]

        conn.close()
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
    return render_template('admin.html', stats=stats)

@app.route('/claims', methods=['GET', 'POST'])
def claims_portal():
    claims = None
    if request.method == 'POST':
        claim_id = request.form.get('claim_id')
        new_status = request.form.get('new_status')
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Update claim status
            cursor.execute("""
                UPDATE claims
                SET claim_status = %s
                WHERE claim_id = %s;
            """, (new_status, claim_id))

            conn.commit()
            flash("Claim status updated successfully!", "success")

            # Fetch all claims
            cursor.execute("SELECT * FROM claims;")
            claims = cursor.fetchall()
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
        finally:
            conn.close()
    return render_template('claims.html', claims=claims)

@app.route('/payments', methods=['GET', 'POST'])
def payments_portal():
    payments = None
    if request.method == 'POST':
        policy_id = request.form.get('policy_id')
        try:
            conn = get_connection()
            cursor = conn.cursor()

            # Fetch payments for a policy
            cursor.execute("""
                SELECT payment_id, payment_date, amount, payment_method, payment_status
                FROM payments
                WHERE policy_id = %s;
            """, (policy_id,))
            payments = cursor.fetchall()
            conn.close()
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
    return render_template('payments.html', payments=payments)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)

