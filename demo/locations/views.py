from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from locations.models import Location, SearchResult
from urllib.request import urlopen
import requests
import json

# Create your views here.

class SearchingLocation(TemplateView):
    template_name = "find_location.html"

def find(request):
    query = str(request.GET.get('q'))
    url = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=' + query
    print("find url: ", url)
    checkurl = requests.get(url)
    if (checkurl.status_code == 200):
        response = checkurl.json()
        for record in response:
            target = SearchResult(nameZH=str(record["nameZH"]), nameEN=str(record["nameEN"]), addressZH=str(record["addressZH"]), addressEN=str(record["addressEN"]), x=int(record["x"]), y=int(record["y"]))
            target.save()
        return render(request, 'results.html', {'response':response})
    else:
        return render(request, 'failure.html')

def save(request):
    if ('save' in request.GET):
        for record in SearchResult.objects.all():
            target = Location(nameZH=str(record.nameZH), nameEN=str(record.nameEN), addressZH=str(record.addressZH), addressEN=str(record.addressEN), x=int(record.x), y=int(record.y))
            target.save()
        for recorded in SearchResult.objects.all():
            recorded.delete()
        return render(request, 'confirmation.html')
    else:
        for recorded in SearchResult.objects.all():
            recorded.delete()
        return render(request, 'find_location.html')
