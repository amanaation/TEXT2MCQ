# from django.http import HttpResponse
from django.shortcuts import render


def display_index(request):
    return render(request, "index.html")
