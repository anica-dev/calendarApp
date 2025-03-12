from django.db import models

class ScrapedData(models.Model):
    event_name = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    event_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name  # Defines a readable representation of the object
