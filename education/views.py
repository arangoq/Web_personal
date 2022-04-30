from django.shortcuts import render
from .models import Education

def education(request):
    education = Education.objects.all()
    return render(request, "education/education.html", {'education':education})