from django.shortcuts import render
from .models import Experience

def experience(request):
    experience = Experience.objects.all()
    return render(request, "experience/experience.html", {'experience':experience})