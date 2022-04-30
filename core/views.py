from django.shortcuts import render
from .models import Core

def core(request):
    core = Core.objects.all()
    return render(request, "core/base.html", {'core':core})
