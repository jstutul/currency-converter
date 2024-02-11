from flask import Flask, jsonify, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# Function to serve flag images
@app.route('/flags/<path:filename>', methods=['GET'])
def get_flag(filename):
    return send_from_directory('static', filename)

# Database file
db_file = "db.sqlite3"

# Connect to the SQLite database
def connect_to_database():
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return None

# Route to fetch countries data
@app.route('/countries', methods=['GET'])
def get_countries():
    try:
        connection = connect_to_database()
        cursor = connection.cursor()
        # Execute query to fetch country data
        cursor.execute('''SELECT country_name, country_lg_name, flags FROM countries''')
        # Fetch all rows
        rows = cursor.fetchall()
        # Close cursor and connection
        cursor.close()
        connection.close()
        # Prepare response JSON
        countries = []
        for row in rows:
            short_name, large_name, flag_file = row
            if flag_file:  # Check if flag_file is not None
                # Construct the file path for the flag image
                flag_path = f'/static/flags/{flag_file}'
            else:
                flag_path = None
            # Create a dictionary for each country
            country = {
                'short_name': short_name,
                'large_name': large_name,
                'flags': flag_path
            }
            countries.append(country)
        return jsonify(countries)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
