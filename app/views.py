from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def near_100_view(request, n):
    return HttpResponse(abs(100 - n) <= 10)
