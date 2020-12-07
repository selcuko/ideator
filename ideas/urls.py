from django.urls import path
from .views import *

app_name = 'ideas'
urlpatterns = [
    path('i/<slug:slug>/', IdeaDetail.as_view(), name='idea-detail'),
    path('ideas/', IdeaList.as_view(), name='idea-list'),
]