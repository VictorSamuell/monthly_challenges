from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Processar os requests e gerar o response
def index(request):
    return HttpResponse("Hello, world. You're at the challenges index.")