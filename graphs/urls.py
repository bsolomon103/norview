from django.urls import path, include
from .views import  SankeyView, TreeView, TableView, ScatterView, DonutView, Download, Redraw

app_name = 'graphs'
urlpatterns = [
    path('sankey/', SankeyView.as_view(), name='sankey'),
    path('tree/', TreeView.as_view(), name='tree'),
    path('table/', TableView.as_view(), name='table'),
    path('scatter/', ScatterView.as_view(), name='scatter'),
    path('donut/', DonutView.as_view(), name='donut'),
    path('<str:file_name>/<str:endpoint>', Download.as_view(), name='download'),
    path('redraw/<str:endpoint>/', Redraw.as_view(), name='redraw'),
    ]