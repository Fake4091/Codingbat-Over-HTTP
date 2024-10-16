from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def near_100_view(request: HttpRequest, n) -> HttpResponse:
    return HttpResponse(abs(100 - n) <= 10)


def string_splosion_view(request: HttpRequest, splode) -> HttpResponse:
    newString = ""

    for i in range(len(splode)):
        newString += splode[0 : i + 1]

    return HttpResponse(newString)


def cat_dog_view(request: HttpRequest, word) -> HttpResponse:
    if word.count("cat") == word.count("dog"):
        return HttpResponse(True)
    return HttpResponse(False)
