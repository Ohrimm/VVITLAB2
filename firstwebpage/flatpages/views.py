
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse(u'Hello,world!', content_type="text/plain")
def home(request):
    return render(request, 'static_handler.html')



