import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.artforum.com/artguide/place/new-york"

def scrape_artguide_nyc():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    listings = []

    entries = soup.find_all("div", class_="artguide-listing")
    for e in entries:
        try:
            title = e.find("span", class_="artguide-title").get_text(strip=True)
            gallery = e.find("span", class_="artguide-venue").get_text(strip=True)
            dates = e.find("span", class_="artguide-dates").get_text(strip=True)
            link = e.find("a", href=True)["href"]
            listings.append({
                "title": title,
                "gallery": gallery,
                "dates": dates,
                "link": f"https://www.artforum.com{link}"
            })
        except:
            continue

    with open("artguide_nyc.json", "w", encoding="utf-8") as f:
        json.dump(listings, f, indent=2, ensure_ascii=False)

scrape_artguide_nyc()
