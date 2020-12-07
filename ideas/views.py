from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import DetailView, ListView
from .models import *



class IdeaList(ListView):
    model = Idea
    context_object_name = 'ideas'
    template_name = 'ideas/list.html'


class IdeaDetail(DetailView):
    model = Idea
    lookup_field = 'slug'
    context_object_name = 'idea'
    template_name = 'ideas/detail.html'