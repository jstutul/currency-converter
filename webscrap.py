import sqlite3
import requests
from bs4 import BeautifulSoup
import re

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

def fetch_data_from_database(connection):
    try:
        if connection is None:
            print("Not connected to the database.")
            return

        cursor = connection.cursor()
        query = "SELECT id, domain FROM myapp_webscrapingdomainlist WHERE results='' ORDER BY id ASC LIMIT 100;"
        cursor.execute(query)
        rows = cursor.fetchall()
        domains_to_check = []

        for row in rows:
            domain_id, domain_name = row
            domains_to_check.append((domain_id, domain_name))

        cursor.close()
        return domains_to_check

    except sqlite3.Error as err:
        print(f"Error: {err}")

def update_database(connection, updates):
    try:
        cursor = connection.cursor()
        update_query = "UPDATE myapp_webscrapingdomainlist SET results=? WHERE id=?;"
        cursor.executemany(update_query, updates)
        connection.commit()
        print(str(len(updates)), " webscraped records updated.")

    except sqlite3.Error as err:
        print(f"Error: {err}")
        connection.rollback()

    finally:
        if connection:
            cursor.close()

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        domains_to_check = fetch_data_from_database(connection)
        connection.close()

        updates = []

        for domain_id, domain_name in domains_to_check:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
                response = requests.get(domain_name, headers=headers)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    body = soup.find('body')
                    for tag in body(['script', 'style', 'img','css','document']):
                        tag.extract()
                    visible_text = ' '.join(body.stripped_strings)
                    cleaned_text = re.sub(r'\s+', ' ', visible_text)
                    cleaned_text = cleaned_text.replace('"', '').replace("'", '').replace('\n', ' ')
                    truncated_text = cleaned_text[:305000]
                    results = truncated_text.strip()
                else:
                    results = "Website Access Denied"
            except Exception as e:
                results = f"Network Error: {e}"

            updates.append((results, domain_id))

        connection = connect_to_database()
        if connection:
            update_database(connection, updates)
            connection.close()
