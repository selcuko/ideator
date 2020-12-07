from django.urls import path
from .views import *

app_name = 'ideas'
urlpatterns = [
    path('i/<slug:slug>/', IdeaDetail.as_view(), name='detail'),
    path('i/<slug:slug>/edit/', IdeaUpdate.as_view(), name='update'),
    path('ideas/', IdeaList.as_view(), name='list'),
    path('submit/', IdeaCreate.as_view(), name='create'),
]