# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .wiki1 import Main_class
import spacy
import nltk.data
import requests
import re
import unidecode
nltk.download('punkt')

def display_index(request):
    return render(request, "index.html")

def view_name(request):
    if request.method == "POST":
        content = request.POST.get("query")

    m = Main_class()
    values = m.main_func(content)

    #print(values)
    return render(request, "output.html", {"values":values})
    #values = {"aman": "<li>mishr</li><li>mishr</li><li>mishr</li>", "ajsy": "mishr", "akash": "mishr"}
    #return render(request, "index.html", {"values":values})
