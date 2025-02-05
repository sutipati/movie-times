import requests
from bs4 import BeautifulSoup
import json

def scrape_galeries():
    url = "https://galeries.be/en/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Get the first movie we find (for demo)
        movie_section = soup.find('div', class_='movie')  # We'll need to update this selector
        
        if movie_section:
            movie_data = {
                "title": movie_section.find('h2').text.strip(),
                "showtimes": [
                    "14:30",  # These are placeholder times
                    "17:00",  # We'll update with actual scraping
                    "20:30"
                ]
            }
            
            # Save to a JSON file
            with open('movie_data.json', 'w', encoding='utf-8') as f:
                json.dump(movie_data, f, ensure_ascii=False, indent=2)
                
            return movie_data
    except Exception as e:
        print(f"Error scraping: {e}")
        return None

if __name__ == "__main__":
    scrape_galeries()