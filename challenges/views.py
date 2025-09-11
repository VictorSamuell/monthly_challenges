from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-vindo ao site de desafios!")

def indexf(request):
    return HttpResponse("Bem-vindos a Fevereiro")