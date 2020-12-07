from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import View
from ideas.forms import IdeaInlineForm


class Landing(View):
    def get(self, request):
        return render(request, 'landing.html', {'form': IdeaInlineForm()})

    def post(self, request):
        form = IdeaInlineForm(request.POST)
        if not form.is_valid():
            return HttpResponse(form.errors, status=400)
        idea = form.save(commit=False)
        idea.session_key = request.session.session_key
        idea.save()
        return HttpResponseRedirect(redirect_to=reverse('ideas:detail', kwargs={'slug': idea.slug}))