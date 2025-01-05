from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<html>"
                        "<h1>"
                        "Welcome to homepage"
                        "</h1>"
                        "</html>")
