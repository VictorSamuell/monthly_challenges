from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

# def index(request):
#     return HttpResponse("Bem-vindo ao site")

# def january_view(request):
#     return HttpResponse("Bem-vindos a Janeiro")

# def february_view(request):
#     return HttpResponse("Bem-vindos a Fevereiro")

# def march_view(request):
#     return HttpResponse("Bem-vindos a Março")

# def april_view(request):
#     return HttpResponse("Bem-vindos a Abril")

# def may_view(request):
#     return HttpResponse("Bem-vindos a Maio")

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Bem-vindo a Janeiro"
    elif month == "february":
        challenge_text = "Bem-vindo a Fevereiro"
    elif month == "march":
        challenge_text = "Bem-vindo a Março"
    elif month == "april":
        challenge_text = "Bem-vindo a Abril"
    elif month == "may":
        challenge_text = "Bem-vindo a Maio"
    elif month == "june":
        challenge_text = "Bem-vindo a Junho"
    elif month == "july":
        challenge_text = "Bem-vindo a Julho"
    elif month == "august":
        challenge_text = "Bem-vindo a Agosto"
    elif month == "september":
        challenge_text = "Bem-vindo a Setembro"
    elif month == "october":
        challenge_text = "Bem-vindo a Outubro"
    elif month == "november":
        challenge_text = "Bem-vindo a Novembro"
    elif month == "december":
        challenge_text = "Bem-vindo a Dezembro"
    else:
        return HttpResponseNotFound("Mês inválido")
    return HttpResponse(challenge_text)