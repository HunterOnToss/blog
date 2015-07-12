from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context


def basic_one(request):
    view = "basic_one"
    html = "<html><body>this is %s view </body><html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    t = get_template("my_view.html")
    html = t.render(Context({'name': view}))
    return HttpResponse(html)
