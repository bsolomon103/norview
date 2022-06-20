from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse as Response
from .forms import AppendForm
import pandas as pd

# Create your views here.

class AppendView(View):
    template = 'components/append.html'
    def get(self, request, *args, **kwargs):
        form = AppendForm()
        ctx = {'form':form}
        return render(request, self.template, context = ctx)
    
    def post(self, request, *args, **kwargs):
        form = AppendForm(request.POST, request.FILES)
        ctx = {'form':form}
        if form.is_valid():
            data = {}
            file_count = len(request.FILES)
            for a in range(file_count):
                file = form.cleaned_data['data_'+str(a)]
                if file.name[-3:] == 'csv':
                    data['data_'+str(a)] = pd.read_csv(file, encoding='cp1252')
                
            print(data['data_0'].empty, data['data_1'].empty)
            
         
        return render(request, self.template, context=ctx)
            
            
