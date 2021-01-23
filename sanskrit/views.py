from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource,Chapter,Content
# Create your views here.

def index(request):
    index_content = Resource.objects.all()
    context = {
        'index_content': index_content
    }
    return render(request,'sanskrit/index.html', context)

def ramayana(request):
    ramayana_content = Content.objects.all()
    context = {
        'ramayana_content': ramayana_content}
    return render(request, 'sanskrit/ramayana.html', context)
