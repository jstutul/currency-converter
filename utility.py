import sqlite3
import os
import requests
# Database file
db_file = "db.sqlite3"

def connect_to_database():
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return None


def create_countries_table():
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            country_name TEXT
                          );''')

        # Commit the transaction and close the connection
        connection.commit()
        connection.close()
        print("Table 'countries' created successfully.")
    except sqlite3.Error as err:
        print(f"Error: {err}")

def insert_countries(countries):
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Prepare the INSERT query
        insert_query = "INSERT INTO countries (country_name) VALUES (?)"

        # Execute the INSERT query for each country in the list
        cursor.executemany(insert_query, [(country,) for country in countries])

        # Commit the transaction and close the connection
        connection.commit()
        connection.close()
        print("Data inserted successfully.")
    except sqlite3.Error as err:
        print(f"Error: {err}")


def download_country_flags(currency_codes, folder):
    # Base URL for country flags
    base_url = "https://wise.com/web-art/assets/flags/{}.png"
    
    for code in currency_codes:
        # Construct the URL for the country flag
        url = base_url.format(code.lower())
        
        # Download the image using the download_image function
        filename = f"{code.lower()}.svg"
        download_image(url, folder, filename)

def download_image(url, folder, filename):
    try:
        headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
        # Send a GET request to the URL
        response = requests.get(url,headers=headers)
        print(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Create the folder if it doesn't exist
            if not os.path.exists(folder):
                os.makedirs(folder)
            
            # Construct the file path
            filepath = os.path.join(folder, filename)
            
            # Write the image content to a file
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"Image downloaded successfully: {filename}")
        else:
            print(f"Failed to download image: {filename}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {filename}. Error: {e}")



