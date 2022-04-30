from django.shortcuts import render
from .models import Awards

def awards(request):
    awards = Awards.objects.all()
    return render(request, "awards/awards.html", {'awards':awards})