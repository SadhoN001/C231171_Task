from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return HttpResponse("First function succesfull..")

def SecondIn(request):
    return render(request,"index.html")
    