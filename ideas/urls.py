from django.urls import path
from .views import *

app_name = 'ideas'
urlpatterns = [
    path('i/', idea, name='idea-detail'),
]