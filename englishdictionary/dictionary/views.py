import dictionary
from django.shortcuts import render
import googletrans
from googletrans import Translator
import pandas as pd
# Create your views here.


def index(request):
    return render(request,"index.html")



def word(request):
    search = request.GET.get("search")
    translator = Translator()
    word = translator.translate(search,dest="tr")
    meaning = word.text
    context = {
        "meaning": meaning,
        
    }
    return render(request,"word.html", context)