from django.shortcuts import render
from .models import Interest

def interest(request):
    interest = Interest.objects.all()
    return render(request, "interest/interests.html", {'interest':interest})