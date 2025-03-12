from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .scraping import scrape_website  # Import your scraper function
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import ScrapedData
from .serializers import JobSerializer

def home(request):
    return render(request, 'home.html')  # Renders a template

@api_view(['GET'])
def scrape_view(request):
    data = ScrapedData.objects.all()  # Fetch all jobs from the database
    serializer = JobSerializer(data, many=True)  # Convert to JSON
    if data:
        return Response(serializer.data)
    else:
        return HttpResponse('Failed to scrape the website.')

