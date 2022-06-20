from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse as Response
from django.urls import reverse_lazy


class HomeView(View):
    template = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, context={})
        

class VisualizeView(View):
    template = 'pages/visualise.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, context={})
        
        
class CleanView(View):
    template = 'pages/clean.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template, context={})