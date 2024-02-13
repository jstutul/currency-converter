import requests
from bs4 import BeautifulSoup

url = 'https://www.remitly.com/us/en'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the <ul> tag with the specified class names
ul_tag = soup.find('ul', class_='f1lcw40v fofyb9g')

# Find all <li> tags within the <ul> tag
li_tags = ul_tag.find_all('li', class_='f1tf6pud')

# Print the content of each <li> tag
for li_tag in li_tags:
    print(li_tag.text.strip())
