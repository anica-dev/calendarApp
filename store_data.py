import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject.settings")
django.setup()

from scrapingApp.models import ScrapedData  # Import Django model
from scrapingApp.scraping import scrape_website


urls=["https://tickets.efinity.rs/"]
if __name__ == "__main__":
    for url in urls:
        data = scrape_website(url)

        created=ScrapedData.objects.get_or_create(  #store data in the database
            title=data["title"],
            url=data["url"],
        )


