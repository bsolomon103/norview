from django.urls import path, include
from .views import  AppendView

app_name = 'stitch'
urlpatterns = [
    path('append/', AppendView.as_view(), name='append'),
  
    ]