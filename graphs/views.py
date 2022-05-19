# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse as Response
from .forms import SankeyForm, TreeForm, TableForm, ScatterForm, DonutForm
#from .sankey import SankeyMaker
import pandas as pd
from django.core.files.uploadedfile import InMemoryUploadedFile
import magic
from django.http import FileResponse
import os 
from django.urls import reverse_lazy
from .orchestration import OrchestrationLayer


# Create your views here.
class SankeyView(View):
    template = 'components/sankeyform.html'
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        form = SankeyForm()
        ctx = {'form':form}
        return render(request, self.template, context=ctx)
        
    def post(self, request, *args, **kwargs):
        form = SankeyForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['data']
            if file.name[-3:] == 'csv':
                data = pd.read_csv(form.cleaned_data['data'], encoding='cp1252')
            if file.name[-3:] == 'xls':
                data = pd.read_excel(form.cleaned_data['data'], encoding='cp1252')
            columns = form.cleaned_data['columns'].split(',')
            columns = [items.strip() for items in columns]
            file_name = form.cleaned_data['file_name']+'.html'
            self.request.session['file_name'] = file_name
           
            graph = OrchestrationLayer(
                genus = 'Sankey',
                data = data,
                file_name = form.cleaned_data['file_name'],
                figure_title = form.cleaned_data['figure_title'],
                columns = columns,
                exclude_column = form.cleaned_data['exclude_column'],
                exclude_value = form.cleaned_data['exclude_value'],
                filter_column = form.cleaned_data['filter_column'],
                filter_value = form.cleaned_data['filter_value']
                      )
            graph = graph.build()
          
        else:
            print('invalid')
        return render(request, self.template, context={'graph':graph, 'name': file_name})

class TreeView(View):
    template = 'components/treeform.html'
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        form = TreeForm()
        ctx = {'form':form}
        return render(request, self.template, context=ctx)
    
    def post(self, request, *args, **kwargs):
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['data']
            if file.name[-3:] == 'csv':
                data = pd.read_csv(form.cleaned_data['data'], encoding='cp1252')
            if file.name[-3:] in ['lsx','xls']:
                data = pd.read_excel(form.cleaned_data['data'])
            columns = form.cleaned_data['columns'].split(',')
            columns = [items.strip() for items in columns]
            file_name = form.cleaned_data['file_name']+'.html'
            self.request.session['file_name'] = file_name
            hover_data = [form.cleaned_data['hover_data']]
            
            graph = OrchestrationLayer(
                genus = 'Tree',
                data = data,
                file_name = form.cleaned_data['file_name'],
                constant = form.cleaned_data['constant'],
                value = form.cleaned_data['value'],
                hover_data = hover_data,
                cols = columns
                      )
            graph = graph.build()
         
        else:
            print('invalid')
        return render(request, self.template, context={'graph':graph, 'name':file_name})
    
class TableView(View):
    template = 'components/tableform.html'
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        form = TableForm()
        ctx = {'form':form}
        return render(request, self.template, context=ctx)
    
    def post(self, request, *args, **kwargs):
        form = TableForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['data']
            if file.name[-3:] == 'csv':
                data = pd.read_csv(form.cleaned_data['data'], encoding='cp1252')
            if file.name[-3:] in ['lsx','xls']:
                data = pd.read_excel(form.cleaned_data['data'])
            columns = form.cleaned_data['columns'].split(',')
            columns = [items.strip() for items in columns]
            file_name = form.cleaned_data['file_name']+'.html'
            self.request.session['file_name'] = file_name
          
            graph = OrchestrationLayer(
                genus = 'Table',
                data = data,
                file_name = form.cleaned_data['file_name'],
                columns = columns
                      )
            graph = graph.build()
            
        else:
            print('invalid')
        return render(request, self.template, context={'graph':graph, 'name':file_name})

class ScatterView(View):
    template = 'components/scatterform.html'
    def get(self, request, *args, **kwargs):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        form = ScatterForm()
        ctx = {'form':form}
        return render(request, self.template, context=ctx)
    
    def post(self, request, *args, **kwargs):
        form = ScatterForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['data']
            if file.name[-3:] == 'csv':
                data = pd.read_csv(form.cleaned_data['data'], encoding='cp1252')
            if file.name[-3:] in ['lsx','xls']:
                data = pd.read_excel(form.cleaned_data['data'])
            file_name = form.cleaned_data['file_name']+'.html'
            self.request.session['file_name'] = file_name
         
            graph = OrchestrationLayer(
                genus = 'Scatter',
                data = data,
                file_name = form.cleaned_data['file_name'],
                x = form.cleaned_data['x'],
                y = form.cleaned_data['y'],
                color = form.cleaned_data['color'],
                size = form.cleaned_data['size']
                      )
            graph = graph.build()
            
        else:
            print('invalid')
        return render(request, self.template, context={'graph':graph, 'name':file_name})

class DonutView(View):
    template = 'components/donut.html'
   
    
    def get(self, request, *args, **kwargs):
        form = DonutForm()
        ctx = {'form':form}
        return render(request, self.template, context = ctx)
    
    def post(self, request, *args, **kwargs):
        form = DonutForm(request.POST , request.FILES)
        if form.is_valid():
            file = form.cleaned_data['data']
            if file.name[-3:] == 'csv':
                data = pd.read_csv(form.cleaned_data['data'], encoding='cp1252')
            if file.name[-3:] in ['lsx','xls']:
                data = pd.read_excel(form.cleaned_data['data'])
            columns = form.cleaned_data['donuts'].split(',')
            columns = [items.strip() for items in columns]
            file_name = form.cleaned_data['file_name'] +'.html'
            self.request.session['file_name'] = file_name 
           
            
            graph = OrchestrationLayer(
                genus = 'donut',
                data = data,
                file_name = form.cleaned_data['file_name'],
                donuts = columns,
                aggregator = form.cleaned_data['aggregator'],
                title_text = form.cleaned_data['title_text'],
                method = form.cleaned_data['method']
                      )
            graph = graph.build()
            if graph is not None:
                return render(request, self.template, context={'graph':graph, 'name':file_name})
            else:
                graph = '<p><b>Error: For this dataset aggregation using mean/median is impossible, click redraw and use count instead</b></p>'
                return render(request, self.template, context={'graph':graph, 'name':file_name} )
            
            
        else:
            print('invalid')
        return render(request, self.template, context={'graph':graph, 'name': file_name})
        
    
    
class Download(View):
    def get(self, request, file_name, endpoint, *args, **kwargs):
        home_url = reverse_lazy('graphs:%s'%(endpoint))
        try:
            file_pointer = open(file_name, 'r')
            response = Response(file_pointer.read(), content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename=%s' %(file_name) 
            if os.path.exists(file_name):
                os.remove(file_name)
                print(request.session['file_name'])
                return response
        except:
            pass
        return redirect(home_url)
        
        
class Redraw(View):
    def get(self, request, endpoint, *args, **kwargs):
        home_url = reverse_lazy('graphs:%s'%(endpoint))
        file_name = request.session['file_name']
        print(file_name)
        if os.path.exists(file_name):
            os.remove(file_name)
        return redirect(home_url)