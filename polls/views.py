from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, You're at the polls index.")
    return render(request, "landing.html", {})


def index2(request, *args, **kwargs):

    return render(request, "contact.html", {})
