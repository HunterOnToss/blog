from django.shortcuts import render
from django.http.response import HttpResponse


def basic_one(request):
    view = "basic_one"
    html = "<html><body>this is %s view </body><html>" % view
    return HttpResponse(html)
