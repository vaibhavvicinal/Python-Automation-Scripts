import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(url):
    """Scrapes book titles and prices from a target URL and exports to CSV."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return "Failed to retrieve data"
        
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []
    
    # Targeting standard product containers
    for item in soup.find_all('article', class_='product_pod'):
        title = item.h3.a['title']
        price = item.find('p', class_='price_color').text
        books.append({'Title': title, 'Price': price})
        
    df = pd.DataFrame(books)
    df.to_csv('scraped_data.csv', index=False)
    print(f"Successfully scraped {len(books)} items.")
    return df

# Example usage on a public sandbox site
if __name__ == "__main__":
    target_url = "http://books.toscrape.com/"
    scrape_books(target_url)
