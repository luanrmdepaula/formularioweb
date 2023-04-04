import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

# Connect to the MySQL database
cnx = mysql.connector.connect(user='your_username', password='your_password',
                              host='localhost', database='your_database')

# Create a cursor object to interact with the database
cursor = cnx.cursor()

# Create a table to store the data
table_name = 'contacts'
create_table = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INT(11) NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        message TEXT NOT NULL,
        PRIMARY KEY (id)
    )
"""
cursor.execute(create_table)

# Define a Flask app
app = Flask(__name__)

# Define a route to show the web form
@app.route('/')
def form():
    return render_template('form.html')

# Define a route to handle the form submission
@app.route('/', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Store the data in the database
    insert_data = f"""
        INSERT INTO {table_name} (name, email, message)
        VALUES ('{name}', '{email}', '{message}')
    """
    cursor.execute(insert_data)
    cnx.commit()

    # Redirect to a thank you page
    return redirect(url_for('thankyou'))

# Define a route for the thank you page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


