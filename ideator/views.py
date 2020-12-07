from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.views.generic import View


class Landing(View):
    def get(self, request):
        return render(request, 'landing.html')
