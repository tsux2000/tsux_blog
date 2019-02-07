from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class MainView(TemplateView):

    def __init__(self):
        self.params = {
            'key' : 'value',
        }

    def get(self, request):
        return render(request, 'main/index.html', self.params)

    def post(self, request):
        return render(request, 'main/index.html', self.params)

    def index(self, request):
        return render(request, 'main/index.html', self.params)
