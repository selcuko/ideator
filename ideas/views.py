from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def idea(request):
    return HttpResponse(timezone.now())