from django.shortcuts import render
from .models import Skills

def skills(request):
    skills = Skills.objects.all()
    return render(request, "skills/skills.html", {'skills':skills})