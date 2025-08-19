import requests
from bs4 import BeautifulSoup

url = "https://joshitha0704.github.io/florell-perfumes/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    print("Scraping successful! Here is all the text content from the page:\n")

    body_content = soup.find('body')
    if body_content:
        all_text = body_content.get_text(separator="\n", strip=True)
        print(all_text)
    else:
        print("Body content not found on the page.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
