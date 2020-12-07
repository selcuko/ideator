from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import *
from .forms import IdeaForm



class IdeaList(ListView):
    model = Idea
    context_object_name = 'ideas'
    template_name = 'ideas/list.html'



class IdeaDetail(DetailView):
    model = Idea
    lookup_field = 'slug'
    context_object_name = 'idea'
    template_name = 'ideas/detail.html'

    def get_context_data(self, *args, **kwargs):
        if not self.request.session.session_key: 
            self.request.session.save()
        ctx = super().get_context_data(*args, **kwargs)
        ctx['authorized'] = (self.request.session.session_key == self.object.session_key) and not bool(self.request.session.session_key)
        return ctx


class IdeaCreate(CreateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/create.html'

    def form_valid(self, form):
        if not self.request.session.session_key: 
            self.request.session.save()
        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)


class IdeaUpdate(UpdateView):
    model = Idea
    form_class = IdeaForm
    template_name = 'ideas/create.html'


    def form_valid(self, form):
        if not self.request.session.session_key: 
            self.request.session.save()
        if not (self.request.session.session_key == self.object.session_key) and not bool(self.request.session.session_key):
            return HttpResponse(status=403)

        form.instance.session_key = self.request.session.session_key
        return super().form_valid(form)

