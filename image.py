import os
import sqlite3

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

# Path to the directory containing the SVG and PNG files
directory_path = r'C:\Users\User\Desktop\currency converter\flags'

# Iterate over the files in the directory
for filename in os.listdir(directory_path):
    if os.path.isfile(os.path.join(directory_path, filename)):
        connection = connect_to_database()
        cursor = connection.cursor()
        # Extract the currency code from the filename
        currency_code = filename.split('.')[0].upper()
        print(filename)
        print(currency_code)
        # Update the flags in the database
        sql = '''UPDATE countries 
                 SET flags = ? 
                 WHERE country_name = ?'''
        params = (filename, currency_code)
        print(sql)
        print(params)
        cursor.execute(sql, params)
        connection.commit()
        cursor.close()
        connection.close()
