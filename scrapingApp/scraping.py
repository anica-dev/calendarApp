from datetime import datetime

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract the website title as an example
        title = soup.title.string if soup.title else "No Title Found"
        url = soup.url if soup.url else "No URL found"
        event_div = soup.find("div", class_="card-body card-body-custom")
        event_name=event_div.find("div").find("h1")
        location=event_div.find("span")
        h3=event_div.find("h3")
        for svg in h3.find_all("svg"):
            svg.extract()  # This removes the <svg> tag
        # Get the remaining text
        date = h3.text.strip()
        event_date= datetime.strptime(date, "%d.%m.%Y.")
        return {"event_name": event_name, "url": url, "event_date":event_date, "location": location}
    else:
        return {"error": f"Failed to fetch {url}, status code: {response.status_code}"}

