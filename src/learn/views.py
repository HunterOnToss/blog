from django.shortcuts import render_to_response


def learn(request):
    return render_to_response("learn.html")
