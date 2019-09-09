from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(response):
    template = 'Home/index.html'
    context = {'title': 'Index'}
    return render(request, template, context) 

class Index(View):
    template = 'Home/index.html'
    context = {'title': 'Index'}
    
    #get method for http.
    def get(self, request):
        return render(request, self.template, self.context)

class About(View):
    template = 'Home/about.html'
    context = {'title': 'About Me'}

    def get(self, request):
        return render(request, self.template, self.context)