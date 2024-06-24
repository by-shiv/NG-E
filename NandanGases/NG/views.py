from urllib import request
from django.http import HttpResponse 
from django.shortcuts import render 
from django.views import View

# Create your views here.

def home(request):
    return render(request,"NG/home.html")

class Shopview(View):
    def get(self, request):
        return render(request,"NG/shop.html")


def about(request):
    return render(request,"NG/about.html")
